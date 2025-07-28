
# 🧪 Photo or Text to 3D Model Generator (Prototype)

A Python + Streamlit app that turns:

* 📷 A **photo of a single object** (e.g., chair, toy, car)
* 📝 Or a **short text description** (e.g., "a small toy car")

→ into a simple **3D model** (`.stl` or `.obj`) for preview or 3D printing.

## 📁 Project Structure

```
photo-text-to-3d/
├── streamlit_app.py         # ✅ Web app (Streamlit Cloud entry point)
├── main.py                  # CLI version (optional)
├── utils/
│   ├── image_processing.py  # Image → 3D model logic
│   ├── text_to_3d.py        # Text → 3D shape generator
│   └── visualizer.py        # 3D visualizer (for local use only)
├── outputs/                 # Saved 3D models (.obj/.stl)
├── requirements.txt         # Dependencies
└── README.md
```

---

## ⚙️ How It Works

### 1. Input Options

* **Option 1**: Upload a `.jpg` or `.png` image of an object
* **Option 2**: Enter a short descriptive prompt (e.g. `"A red toy car"`)

### 2. Processing

* 📸 **Image Input**:

  * Removes background using [`rembg`](https://github.com/danielgatis/rembg)
  * Converts object shape into 3D point cloud and mesh using `trimesh`
* 🧠 **Text Input**:

  * Maps common nouns to primitives: box, sphere, cylinder
  * Generates basic 3D geometry

### 3. Output

* Saves a `.obj` or `.stl` file in the `outputs/` folder
* On Streamlit, provides a **download link**

---

## 🖥️ Local Installation

### 🔧 Step 1: Clone this repo

```bash
git clone https://github.com/yourusername/photo-text-to-3d.git
cd photo-text-to-3d
```

### 🐍 Step 2: Set up virtual environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 📦 Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Locally

### 🖥️ Terminal (CLI version):

```bash
python main.py
```

You’ll see:

```
🧪 3D Model Generator
---------------------
1. Image to 3D
2. Text to 3D
Choose an option (1 or 2):
```

### 🌐 Streamlit App (Web version):

```bash
streamlit run streamlit_app.py
```

---

## 📂 Example Inputs

| Input Type | Example             | Output                     |
| ---------- | ------------------- | -------------------------- |
| Image      | `car.png`           | `outputs/model_<uuid>.obj` |
| Text       | `"a small toy car"` | `outputs/model_<uuid>.obj` |

---

## 🧠 Thought Process

* Minimalistic prototype logic for fast testing
* Modular design: separate files for image, text, and visualization
* Easily extendable with AI 3D models like [Shap-E](https://github.com/openai/shap-e), [Point-E](https://github.com/openai/point-e), or [DreamFusion](https://dreamfusion3d.github.io)

---

## 🔧 Tech Stack

| Tool                      | Purpose                        |
| ------------------------- | ------------------------------ |
| `streamlit`               | Web frontend                   |
| `rembg`                   | Background removal from images |
| `trimesh`                 | 3D model creation/export       |
| `numpy`, `Pillow`, `uuid` | Utilities                      |
| `opencv-python-headless`  | Image decoding                 |

---

## ✅ Example Output Files

All generated `.obj` / `.stl` files are saved in:

```
outputs/
```

---

## 💡 Future Plans

* Integrate advanced AI text-to-3D models (e.g., Shap-E, Point-E)
* Improve mesh generation from images (depth estimation, segmentation)
* Support model preview on Streamlit using `stpyvista`, `three.js`, or `vtk.js`

---

## 📬 Feedback & Contributions

Feel free to open issues, submit PRs, or fork the project!

