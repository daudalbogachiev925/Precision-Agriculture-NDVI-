import numpy as np

def compute_ndvi(nir, red, eps=1e-6):
    """NDVI = (NIR - Red) / (NIR + Red), диапазон [-1, 1]."""
    return (nir - red) / (nir + red + eps)

def classify_ndvi(ndvi):
    """
    Классы:
    < 0    — вода/искусственные
    0-0.2  — почва/стресс
    0.2-0.4 — разреженная растительность
    0.4-0.6 — умеренная
    > 0.6  — здоровая
    """
    classes = np.zeros_like(ndvi, dtype=np.uint8)
    classes[ndvi < 0] = 1
    classes[(ndvi >= 0) & (ndvi < 0.2)] = 2
    classes[(ndvi >= 0.2) & (ndvi < 0.4)] = 3
    classes[(ndvi >= 0.4) & (ndvi < 0.6)] = 4
    classes[ndvi >= 0.6] = 5
    return classes
