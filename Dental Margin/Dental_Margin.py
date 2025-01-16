import tkinter as tk
from tkinter import filedialog, messagebox
import trimesh
import open3d as o3d
import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt

def load_stl(file_path):
    try:
        print(f"Loading STL file: {file_path}")
        mesh = trimesh.load(file_path)
        if len(mesh.faces) == 0:
            raise ValueError("Mesh has no faces (triangles)")
        if len(mesh.vertices) == 0:
            raise ValueError("Mesh has no vertices")
        print(f"STL file '{file_path}' is valid.")
        print(f"Number of faces (triangles): {len(mesh.faces)}")
        print(f"Number of vertices: {len(mesh.vertices)}")
        return mesh
    except Exception as e:
        print(f"An error occurred while validating STL file with Trimesh: {e}")
        return None

def mesh_to_point_cloud(mesh, number_of_points=10000):
    mesh_o3d = o3d.geometry.TriangleMesh()
    mesh_o3d.vertices = o3d.utility.Vector3dVector(mesh.vertices)
    mesh_o3d.triangles = o3d.utility.Vector3iVector(mesh.faces)
    if not mesh_o3d.has_vertex_normals():
        mesh_o3d.compute_vertex_normals()
    return mesh_o3d.sample_points_uniformly(number_of_points)

def detect_edges(points):
    kdtree = KDTree(points)
    edges = []
    for point in points:
        distances, indices = kdtree.query(point, k=10)
        local_points = points[indices]
        cov_matrix = np.cov(local_points.T)
        eigvals, _ = np.linalg.eigh(cov_matrix)
        if eigvals[0] < 0.01:
            edges.append(point)
    return np.array(edges)

def fit_margin_curve(edges):
    edges = edges[np.argsort(edges[:, 0])]
    z = np.polyfit(edges[:, 0], edges[:, 1], 5)
    return np.poly1d(z)

def visualize_margin(edges, margin_curve):
    plt.scatter(edges[:, 0], edges[:, 1], c='r', label='Detected edges')
    x = np.linspace(min(edges[:, 0]), max(edges[:, 0]), 500)
    plt.plot(x, margin_curve(x), 'b-', label='Fitted curve')
    plt.legend()
    plt.show()

def run_margin_detection(file_path):
    mesh = load_stl(file_path)
    if mesh is None:
        messagebox.showerror("Error", "Invalid STL file. Please select a valid file.")
        return

    point_cloud = mesh_to_point_cloud(mesh)
    points = np.asarray(point_cloud.points)

    edges = detect_edges(points)
    margin_curve = fit_margin_curve(edges)
    visualize_margin(edges, margin_curve)

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("STL files", "*.stl")])
    if file_path:
        file_path_var.set(file_path)
        run_margin_detection(file_path)

def submit_rating():
    rating = rating_var.get()
    messagebox.showinfo("Rating Submitted", f"You rated the margin detection as {rating}")

# Create the main window
root = tk.Tk()
root.title("STL Margin Detection")

# File selection
file_path_var = tk.StringVar()
tk.Label(root, text="Select STL file:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=file_path_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=10, pady=10)

# Rating
rating_var = tk.IntVar()
tk.Label(root, text="Rate the margin detection (1-5):").grid(row=1, column=0, padx=10, pady=10)
for i in range(1, 6):
    tk.Radiobutton(root, text=str(i), variable=rating_var, value=i).grid(row=1, column=i, padx=5, pady=10)

# Submit button
tk.Button(root, text="Submit Rating", command=submit_rating).grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Start the main loop
root.mainloop()
