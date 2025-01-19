# src/model.py
import numpy as np


def predict(features):
    """Mock prediction function."""
    return np.sum(features)


if __name__ == "__main__":
    sample_features = [1.5, 2.5, 3.5]
    print(f"Prediction: {predict(sample_features)}")
    