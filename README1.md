<div align="center">

# xhec-mlops-project-student

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue.svg)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: flake8](https://img.shields.io/badge/linting-flake8-blue)](https://github.com/PyCQA/flake8)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-informational?logo=pre-commit&logoColor=white)](https://github.com/artefactory/xhec-mlops-project-student/blob/main/.pre-commit-config.yaml)
</div>

This repository has for purpose to industrialize the [Abalone age prediction](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) Kaggle contest.

<details>
<summary>Details on the Abalone Dataset</summary>

The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope -- a boring and time-consuming task. Other measurements, which are easier to obtain, are used to predict the age.

**Goal**: predict the age of abalone (column "Rings") from physical measurements ("Shell weight", "Diameter", etc...)

</details>

## Table of Contents
1. [Project Overview](#project-overview)
2. [Folder Structure](#folder-structure)
3. [Installation](#installation)
4. [Training the Model](#training-the-model)
5. [Using Docker](#using-docker)
6. [Using the API](#using-the-api)
7. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
8. [Contributors](#contributors)

---

## Project Overview

This project is centered around predicting the number of rings in abalones, which can be used to estimate the age of the abalone. We trained a **Linear Regression model** on a dataset of physical measurements of abalones, and we provide the following components:

- An **EDA notebook** showcasing initial analysis and visualization of the dataset.
- A **FastAPI** web service for model inference.
- An **orchestration workflow** using **Prefect** to automate the training and deployment process.
- A **Docker** container for easy deployment of the model and API.

---

## Folder Structure

Here is the structure of the project:

```
project/
├── .github/
│   └── workflows/
│       └── ci.yaml               # GitHub Actions CI workflow file
├── data/
│   └── abalone.csv               # The dataset file used for model training
├── notebooks/
│   ├── eda.ipynb                 # Jupyter notebook for Exploratory Data Analysis (EDA)
│   └── modelling.ipynb           # Jupyter notebook for model building and testing
├── src/
│   └── modelling/
│       ├── main.py               # Entry point for running the project
│       ├── predicting.py         # Handles prediction using the trained model
│       ├── preprocessing.py      # Preprocessing steps for the dataset
│       ├── training.py           # Code for training the model
│       └── utils.py              # Utility functions used in the project
├── web_service/
│   └── local_objects/
│       ├── .gitkeep              # Placeholder to ensure folder tracking in Git
│       └── model.pkl             # Serialized model (trained Linear Regression model)
├── .gitignore                    # Files and directories to be ignored by Git
├── .pre-commit-config.yaml       # Pre-commit hooks configuration
├── README.md                     # Documentation of the project
├── config.py                     # Configuration settings for the project
├── environment.yml               # Conda environment configuration file
├── orchestration.py              # Prefect orchestration script for model deployment
├── pyproject.toml                # Project configuration (includes linting and formatting tools)
├── requirements-dev.in           # Development dependencies input for pip-tools
├── requirements-dev.txt          # Development dependencies generated by pip-tools
├── requirements.in               # Base dependencies input for pip-tools
├── requirements.txt              # Production dependencies generated by pip-tools
```

---

## Installation

To set up the environment for this project, follow the steps below:

### 1. Clone the Repository

```bash
git clone https://github.com/jazmnm/xhec-mlops-project-student.git
cd project
```

### 2. Create and Activate a Virtual Environment

It's recommended to create a virtual environment for this project:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```
If you use conda, refer to the next step for environment setup. 

### 3. Install Dependencies

You can set up the environment for this project using either **pip** or **conda**.

#### Option 1: Using Conda

If you prefer using **conda** for managing environments, follow these steps:

1. **Create and Activate the Environment**

   Create a new conda environment based on the `environment.yml` file:

   ```bash
   conda env create -f environment.yml
   conda activate your-env-name  # Replace with the environment name specified in environment.yml
   ```

2. **Install Additional Development Dependencies**

   If you want to install the development dependencies as well (for linting, testing, etc.), you can install them from the `requirements-dev.txt` file:

   ```bash
   pip install -r requirements-dev.txt
   ```

#### Option 2: Using pip

If you prefer using **pip** for managing dependencies, you can follow this approach:

1. **Create a Virtual Environment**

   You can use Python's built-in `venv` module to create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

2. **Install the Required Packages**

   For production use (minimal dependencies), install the packages from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Development Dependencies**

   If you're working in a development environment, install additional dependencies from `requirements-dev.txt`:

   ```bash
   pip install -r requirements-dev.txt
   ```

#### Option 3: Install from Input Files (pip-tools)

If you are using **pip-tools** to manage dependencies, you can install from the input `.in` files:

1. **Install pip-tools**

   First, install pip-tools:

   ```bash
   pip install pip-tools
   ```

2. **Compile the Requirements**

   If you need to update `requirements.txt` or `requirements-dev.txt`, you can recompile them from the `.in` files:

   ```bash
   pip-compile requirements.in
   pip-compile requirements-dev.in
   ```

3. **Install from `.in` Files**

   You can directly install the base and development dependencies from the `.in` files if needed:

   ```bash
   pip-sync requirements.txt requirements-dev.txt
   ```

---

### Additional Notes:

- **Production**: Use `requirements.txt` if you just want to run the application with minimal dependencies.
- **Development**: Use `requirements-dev.txt` if you want to contribute to the project (includes linting, testing tools).
- **Conda Users**: Use `environment.yml` to set up everything at once, and then you can install additional tools with pip if necessary.

### Summary of Environment Files:
- **`requirements.in`**: Base dependencies input for pip-tools.
- **`requirements.txt`**: Production-ready dependencies generated from `requirements.in`.
- **`requirements-dev.in`**: Development dependencies input for pip-tools.
- **`requirements-dev.txt`**: Development dependencies generated from `requirements-dev.in`.
- **`environment.yml`**: Conda environment configuration for setting up both production and development environments.

---

## Orchestration

The orchestration...

---

## Using Docker

The project is set up for deployment using **Docker**. You can build and run the Docker container to serve the model with **FastAPI**.

### 1. Build the Docker Image

```bash
docker build -t abalone-model .
```

### 2. Run the Docker Container

```bash
docker run -d -p 8000:8000 abalone-model
```

This will start the FastAPI app, which you can access at `http://localhost:8000`.

---

## Using the API

The FastAPI app provides an endpoint to make predictions. Once the Docker container is running, you can make a `POST` request to the `/predict` endpoint.

### Sample Request:

```bash
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{
    "feature1": 1.0,
    "feature2": 2.0
}'
```

### Sample Response:

```json
{
  "prediction": 10.5
}
```

This will return the predicted number of rings for the abalone based on the input features.

---

## Exploratory Data Analysis (EDA)

The project includes an **EDA notebook** that provides insights into the dataset. You can find it in the `eda/eda_notebook.ipynb` file.

---

## Contributors

- **Xianghan Mei**
- **Teammate 1**
- **Teammate 2**
- **Teammate 3**

---