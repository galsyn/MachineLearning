import numpy as np
def angle_teta_rad(ar1, ar2):
    dot_production = np.dot(ar1, ar2)
    cos_teta = dot_production / np.linalg.norm(ar1) / np.linalg.norm(ar2)
    return round(np.arccos(cos_teta), 4)


def angle_teta180(ar1, ar2):
    dot_production = np.dot(ar1, ar2)
    cos_teta = dot_production / np.linalg.norm(ar1) / np.linalg.norm(ar2)
    return round(np.arccos(cos_teta) * 180 / np.pi, 2)

