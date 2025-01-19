# MLOps Pipeline

This repository demonstrates a simple MLOps CI/CD pipeline using GitHub Actions.

## Features
- Linting with `flake8`
- Unit testing with `pytest`
- Example ML model script

## Directory Structure

mlops-pipeline/
├── .github/
│   └── workflows/
│       └── mlops-ci.yml   # GitHub Actions workflow file
├── src/
│   └── model.py           # A simple ML model script
├── tests/
│   └── test_model.py      # Unit tests for the model
├── requirements.txt       # Dependencies
└── README.md              # Project description
