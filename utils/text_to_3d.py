import trimesh


def generate_3d_from_text(prompt: str, output_path: str) -> None:
    """
    Placeholder: Generates a simple 3D primitive mesh based on prompt keywords.

    Args:
        prompt (str): Text description (e.g., "a small red toy car")
        output_path (str): File path to save .obj or .stl
    """
    prompt = prompt.lower()

    if "sphere" in prompt or "ball" in prompt:
        mesh = trimesh.creation.icosphere(radius=1.0)
    elif "car" in prompt:
        mesh = trimesh.creation.box(extents=[2, 1, 0.5])
    elif "chair" in prompt:
        mesh = trimesh.creation.box(extents=[1, 1, 1])
    else:
        # Default primitive
        mesh = trimesh.creation.cylinder(radius=0.5, height=1.5)

    mesh.export(output_path)
