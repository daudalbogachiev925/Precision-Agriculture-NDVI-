import cv2
import numpy as np

def stitch(images):
    stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)
    status, pano = stitcher.stitch(images)
    if status != cv2.Stitcher_OK:
        raise RuntimeError(f"Stitching failed: {status}")
    return pano

def colorize_ndvi(ndvi):
    norm = np.clip((ndvi + 1) / 2, 0, 1)
    img = (norm * 255).astype(np.uint8)
    return cv2.applyColorMap(img, cv2.COLORMAP_RdYlGn)
