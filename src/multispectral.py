import cv2
import numpy as np

class MultispectralLoader:
    """Загрузка NIR + RGB каналов."""
    def load(self, nir_path, red_path):
        nir = cv2.imread(nir_path, cv2.IMREAD_GRAYSCALE)
        red = cv2.imread(red_path, cv2.IMREAD_GRAYSCALE)
        if nir is None or red is None:
            raise FileNotFoundError("Не удалось загрузить каналы")
        return nir.astype(np.float32), red.astype(np.float32)
