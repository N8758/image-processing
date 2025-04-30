# 🧪 Photo or Text to 3D Model Generator (Prototype)

This project is a Python-based prototype that converts either:
- A **photo** of a single object (e.g., chair, toy, car), or
- A **text description** (e.g., "a small toy car")

into a simple 3D model (`.stl` or `.obj`) that can be visualized or exported for 3D printing.

---

## 📁 Project Structure

```
photo-text-to-3d/
├── main.py                 # Main entry script
├── utils/
│   ├── image_processing.py # Image → 3D logic (background removal, basic shape)
│   ├── text_to_3d.py       # Text prompt → 3D shape generation
│   └── visualizer.py       # Simple 3D visualizer using trimesh
├── outputs/                # All generated 3D models are saved here
├── requirements.txt        # All dependencies
└── README.md               # You're reading this!
```

---

## 🚀 How It Works

### 1. **Input**
You can choose:
- **Option 1:** Upload an image of a single object (e.g. `car.png`)
- **Option 2:** Enter a short descriptive text (e.g. "A red toy car")

---

### 2. **Processing**
- **For Images:**
  - Uses `rembg` to remove the background
  - Converts the image to a basic 3D shape using point sampling
- **For Text:**
  - Simple logic maps key nouns/keywords to basic 3D primitives (cube, sphere, etc.)

---

### 3. **Output**
- A `.stl` or `.obj` 3D file is saved in the `outputs/` folder
- You also get a live 3D preview of the model using `trimesh`

---

## 📦 Installation

### Step 1: Clone this repository
```bash
git clone https://github.com/yourusername/photo-text-to-3d.git
cd photo-text-to-3d
```

### Step 2: Create & activate virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Once dependencies are installed:

```bash
python main.py
```

You’ll be prompted to:
```
🧪 3D Model Generator
---------------------
1. Image to 3D
2. Text to 3D
Choose an option (1 or 2):
```

---

## 📥 Example Inputs

### ✅ Option 1: Image
- Provide the path to a `.jpg` or `.png` file
- Output: `outputs/generated_model.stl` or `.obj`
- Visualization window opens automatically

### ✅ Option 2: Text
- Enter: `"a small toy car"`
- Output: simple 3D shape file
- Live viewer shows result

---

## 🧠 Thought Process & Architecture

- I prioritized simplicity and prototype-readiness.
- Image input is handled with `rembg` for clean object extraction.
- Text input maps basic nouns to shapes using deterministic rules.
- The output uses `trimesh` for easy STL/OBJ creation and preview.
- The system is modular and can be extended later with AI models like **Shap-E**, **Point-E**, or **DreamFusion**.

---

## 🛠️ Libraries Used

- [`rembg`](https://github.com/danielgatis/rembg): Background removal
- `trimesh`: 3D mesh creation and visualization
- `numpy`, `Pillow`: Image and math handling
- `uuid`: For generating unique filenames

---

## ✅ Example Output Files

You can find sample generated `.stl` or `.obj` files in:
```
/outputs/
```

---

## 💡 Future Improvements

- Integrate advanced open-source text-to-3D models (e.g., Shap-E, Point-E)
- Improve geometry extraction from images
- Deploy this as a web app (e.g., using FastAPI + Three.js frontend)

---



---

