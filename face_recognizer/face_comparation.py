import numpy as np

def is_features_matched(features1, features2, threshold=80.0):
    distance = np.linalg.norm(features1 - features2)
    return distance < threshold