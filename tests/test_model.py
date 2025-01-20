# tests/test_model.py
import os  
import sys
current_directory = os.getcwd()
print("Current Directory:", current_directory)
# current_directory = current_directory+'\mlops-pipeline'
print("Current Directory:", current_directory)
# Get the current working directory
sys.path.append(current_directory)

from src.model import predict


def test_predict():
    features = [1, 2, 3]
    assert predict(features) == 6
