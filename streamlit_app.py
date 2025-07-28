import streamlit as st
import os
import uuid
from utils.image_processing import process_image_to_3d
from utils.text_to_3d import generate_3d_from_text

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

st.title("🧪 Photo or Text to 3D Model Generator")
st.write("Convert an image or text prompt into a simple 3D model (.obj or .stl)")

option = st.radio("Choose input method:", ["Image to 3D", "Text to 3D"])

if option == "Image to 3D":
    uploaded_file = st.file_uploader("Upload a .jpg or .png image", type=["jpg", "png"])
    if uploaded_file is not None:
        filename = f"{uuid.uuid4().hex}.obj"
        filepath = os.path.join("temp_input", filename)
        os.makedirs("temp_input", exist_ok=True)
        with open(filepath, "wb") as f:
            f.write(uploaded_file.read())

        output_path = os.path.join(OUTPUT_DIR, filename)
        process_image_to_3d(filepath, output_path)
        st.success(f"✅ 3D model generated!")
        st.download_button("⬇️ Download .obj", open(output_path, "rb"), file_name=filename)

elif option == "Text to 3D":
    text_prompt = st.text_input("Enter your text (e.g., 'a small red toy car')")
    if st.button("Generate"):
        if text_prompt.strip() == "":
            st.warning("⚠️ Please enter some text.")
        else:
            filename = f"{uuid.uuid4().hex}.obj"
            output_path = os.path.join(OUTPUT_DIR, filename)
            generate_3d_from_text(text_prompt, output_path)
            st.success("✅ 3D model generated from text!")
            st.download_button("⬇️ Download .obj", open(output_path, "rb"), file_name=filename)
