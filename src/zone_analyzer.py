import numpy as np

class ZoneAnalyzer:
    def __init__(self, stress_threshold=0.3):
        self.threshold = stress_threshold

    def analyze(self, ndvi):
        stress_mask = (ndvi < self.threshold) & (ndvi >= 0)
        stress_ratio = stress_mask.mean()
        return {
            "mean_ndvi": float(ndvi.mean()),
            "max_ndvi": float(ndvi.max()),
            "min_ndvi": float(ndvi.min()),
            "stress_ratio": float(stress_ratio),
            "healthy_ratio": float((ndvi > 0.5).mean()),
        }
