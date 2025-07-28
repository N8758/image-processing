import streamlit as st
import os
import uuid
from utils.image_processing import process_image_to_3d
from utils.text_to_3d import generate_3d_from_text
from utils.visualizer import visualize_3d_model

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_unique_filename(extension=".obj"):
    return os.path.join(OUTPUT_DIR, f"{uuid.uuid4().hex}{extension}")

st.title("🧪 3D Model Generator")
option = st.radio("Choose an option:", ["Image to 3D", "Text to 3D"])

if option == "Image to 3D":
    image_file = st.file_uploader("Upload an image file (jpg/png)", type=["jpg", "jpeg", "png"])
    if image_file and st.button("Generate 3D Model"):
        image_path = os.path.join(OUTPUT_DIR, image_file.name)
        with open(image_path, "wb") as f:
            f.write(image_file.read())

        st.info("🖼️ Processing image to 3D model...")
        output_file = get_unique_filename(".stl")
        process_image_to_3d(image_path, output_file)
        st.success(f"✅ 3D model saved: {output_file}")
        visualize_3d_model(output_file)

elif option == "Text to 3D":
    prompt = st.text_input("Enter your text prompt", placeholder="e.g., a small red toy car")
    if prompt and st.button("Generate 3D Model"):
        st.info("🧠 Generating 3D model from text...")
        output_file = get_unique_filename(".obj")
        generate_3d_from_text(prompt, output_file)
        st.success(f"✅ 3D model saved: {output_file}")
        visualize_3d_model(output_file)
