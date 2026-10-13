import numpy as np
from src.ndvi import compute_ndvi

def test_ndvi_healthy():
    nir = np.array([[200.0]])
    red = np.array([[50.0]])
    ndvi = compute_ndvi(nir, red)
    assert ndvi[0, 0] > 0.5

def test_ndvi_water():
    nir = np.array([[50.0]])
    red = np.array([[100.0]])
    assert compute_ndvi(nir, red)[0, 0] < 0
