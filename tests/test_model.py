# tests/test_model.py
import os
import sys
from /home/runner/work/mlops-pipeline/mlops-pipeline/src.model import predict

def test_predict():
    features = [1, 2, 3]
    assert predict(features) == 6
