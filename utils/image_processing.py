import numpy as np
import cv2
import trimesh
from rembg import remove


def process_image_to_3d(image_path: str, output_path: str) -> None:
    """
    Converts a photo of a single object into a basic 3D mesh approximation.
    Background is removed before conversion to 3D.

    Args:
        image_path (str): Path to input image file
        output_path (str): Path to save .stl or .obj file
    """
    # Load and remove background
    with open(image_path, "rb") as f:
        input_bytes = f.read()
    no_bg_bytes = remove(input_bytes)

    # Convert back to image
    nparr = np.frombuffer(no_bg_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    if image.shape[2] != 4:
        raise ValueError("Expected image with alpha channel after background removal.")

    # Generate 3D point cloud from non-transparent pixels
    h, w, _ = image.shape
    pixels = np.argwhere(image[:, :, 3] > 0)  # Use alpha channel
    colors = image[pixels[:, 0], pixels[:, 1], :3] / 255.0

    z = np.ones((pixels.shape[0], 1)) * 0.1  # Dummy depth for simplicity
    xyz = np.hstack((pixels[:, [1, 0]], z))  # (x, y, z)

    # Create mesh from points
    cloud = trimesh.points.PointCloud(xyz, colors)
    mesh = cloud.convex_hull

    mesh.export(output_path)
