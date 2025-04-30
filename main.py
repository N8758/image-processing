import os
import sys
import uuid
from utils.image_processing import process_image_to_3d
from utils.text_to_3d import generate_3d_from_text
from utils.visualizer import visualize_3d_model

OUTPUT_DIR = "outputs"


def ensure_output_folder():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def get_unique_filename(extension=".obj"):
    return os.path.join(OUTPUT_DIR, f"{uuid.uuid4().hex}{extension}")


def handle_image_input():
    image_path = input("Enter path to the image file (jpg/png): ").strip()
    if not os.path.isfile(image_path):
        print("❌ File not found.")
        sys.exit(1)

    print("🖼️ Processing image to 3D model...")
    output_file = get_unique_filename(".stl")
    process_image_to_3d(image_path, output_file)

    print(f"✅ 3D model saved to: {output_file}")
    visualize_3d_model(output_file)


def handle_text_input():
    prompt = input("Enter your text prompt (e.g., 'a small red toy car'): ").strip()
    if not prompt:
        print("❌ Text prompt cannot be empty.")
        sys.exit(1)

    print("🧠 Generating 3D model from text...")
    output_file = get_unique_filename(".obj")
    generate_3d_from_text(prompt, output_file)

    print(f"✅ 3D model saved to: {output_file}")
    visualize_3d_model(output_file)


def main():
    print("🧪 3D Model Generator")
    print("---------------------")
    print("1. Image to 3D")
    print("2. Text to 3D")

    choice = input("Choose an option (1 or 2): ").strip()

    ensure_output_folder()

    if choice == "1":
        handle_image_input()
    elif choice == "2":
        handle_text_input()
    else:
        print("❌ Invalid choice.")
        sys.exit(1)


if __name__ == "__main__":
    main()
