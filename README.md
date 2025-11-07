![image](https://github.com/user-attachments/assets/91a86cb6-b3f3-489a-8d39-443b2298d971)

# 🦷 STL Vertex Analysis GUI

A lightweight, Python-based desktop app for detecting **voxel-based issues** in STL files — with margin detection, smart point cloud sampling, polynomial curve fitting, and a Tkinter-powered GUI.

---

##  What is This?

This app lets you:

-  Load STL files of dental models  
-  Convert mesh to point cloud  
-  Detect potential margin edges using geometry & KDTree  
-  Fit a clean polynomial curve to the edge line  
-  Visualize the result using `matplotlib`  
-  Rate the quality of detection via a GUI  


##  Features

- ✅ STL mesh loading and validation  
- ✅ Convert mesh to point cloud using Open3D  
- ✅ Edge detection via KDTree & covariance analysis  
- ✅ 5th-degree polynomial curve fitting  
- ✅ Margin visualization (red dots + blue curve)  
- ✅ User rating system for feedback  
- ✅ Simple, local GUI using `tkinter` — no web browser needed!

---

##  Tech Stack

- **Core**: Python 3  
- **GUI**: Tkinter  
- **Mesh Handling**: Trimesh  
- **Point Cloud Sampling**: Open3D  
- **Math & Geometry**: NumPy, SciPy  
- **Plotting**: Matplotlib  

---

##  Installation

Make sure Python 3.8+ is installed. Then run:

```bash
pip install trimesh open3d numpy scipy matplotlib


---

##  Features

 Load and validate STL meshes  
 Convert mesh to point cloud using Open3D  
 KDTree + covariance-based edge detection  
 Polynomial curve fitting (5th degree)  
 Visualization of margin and fitted curve  
 User feedback with rating system  
 GUI built in Tkinter — no web browser needed!

---

##  Tech Stack

- **Backend / Core**: Python 3
- **GUI**: Tkinter
- **Mesh processing**: Trimesh
- **Point cloud sampling**: Open3D
- **Math & stats**: NumPy, SciPy
- **Plotting**: Matplotlib

---

##  Installation

Make sure Python 3.8+ is installed, then run this:

```bash
pip install trimesh open3d numpy scipy matplotlib
 How to Use
bash
Copy
Edit
python margin.py
Use the “Browse” button to select an .stl file.

Margin detection and visualization will run automatically.

Rate how accurate you think the detection was (1-5).

Brag about your AI-enhanced margin detection on LinkedIn.

 Under the Hood
STL Loading: via trimesh

Mesh → Point Cloud: using open3d.geometry.TriangleMesh.sample_points_uniformly()

Edge Detection:

KDTree finds nearest neighbors

Covariance matrix of local points

Eigenvalues analyzed — low variance = possible margin

Curve Fitting:

5th-degree polynomial fitted to x/y edge scatter

Visualization: red dots = edges, blue line = curve

 Project Layout
graphql
Copy
Edit
Dental-Margin-analyser/
│
├── margin.py           # Main script (run this!)
├── README.md           # This file
└── sample.stl          # Optional test STL file
 Wishlist / Future Features
Export fitted margin as new STL/OBJ

3D OpenGL viewer (Open3D or PyVista)

Margin accuracy analytics

AI model training for automatic margin classification

Crown auto-design integration

Dark mode for your late-night margin sessions 🌙

 Disclaimers
This is a prototype, not a medical-grade tool.

Works best with high-resolution, clean STL models.

3D geometry is fun, but don’t skip your dental appointments.

👑 Credits
Developed by Zaid at [Links Technologies]
Powered by Python, espresso, and stubbornness.

🪪 License
MIT License. Free to use, modify, and share.
