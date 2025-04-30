import trimesh


def visualize_3d_model(filepath: str) -> None:
    """
    Opens a 3D viewer for the given .obj or .stl file using trimesh.

    Args:
        filepath (str): Path to the 3D model file
    """
    try:
        mesh = trimesh.load(filepath)
        if not isinstance(mesh, trimesh.Trimesh) and hasattr(mesh, 'geometry'):
            # If it's a scene with multiple geometries
            mesh = mesh.dump(concatenate=True)
        mesh.show()
    except Exception as e:
        print(f"❌ Error loading 3D model: {e}")
