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
4. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
5. [Train the Model](#train-the-model)
6. [Using Docker](#using-docker)
7. [Using the API](#using-the-api)
8. [Contributors](#contributors)

---

## Project Overview

This project is centered around predicting the number of rings in abalones, which can be used to estimate the age of the abalone. We trained a **Linear Regression model** on a dataset of physical measurements of abalones, and we provide the following components:

- An **EDA notebook** showcasing initial analysis and visualization of the dataset.
- A **FastAPI** web service for model inference.
- An **Orchestration Workflow** using **Prefect** to automate the training, deployment and scheduled retaining process.
- A **Docker** container for easy deployment of the model and API.

---

## Folder Structure

Here is the structure of the project:

```
project/
├── .github/
│   └── workflows/
│       └── ci.yaml               # GitHub Actions CI workflow file
├── bin
│   └── run_service.sh            # Script for running the dockerized api with prefect
├── data/
│   └── abalone.csv               # The dataset file used for model training
├── notebooks/
│   ├── eda.ipynb                 # Jupyter notebook for Exploratory Data Analysis (EDA)
│   └── modelling.ipynb           # Jupyter notebook for model building and testing
├── src/
│   └── modelling/                # Folder for source codes for model training
│       ├── main.py               # Script for training and saving the trained model
│       ├── predicting.py         # Contains functions related to prediction and evaluation
│       ├── preprocessing.py      # Preprocessing steps for dataset
│       ├── training.py           # Code for training pipeline
│       └── utils.py              # Utility functions used in model training
├── web_service/
│   └── lib/                      # Folder for source codes for api
│       ├── inference.py          # Script for making inference
│       ├── models.py             # Setting pydantic models
│       ├── preprocessing.py      # Preprocessing steps for dataset
│   └── local_objects/
│       ├── .gitkeep              # Placeholder to ensure folder tracking in Git
│       └── model.pkl             # Serialized model (trained Linear Regression model)
│   ├── app_config.py             # API configurations
│   └── main.py                   # Script for building the API
│   └── utils.py                  # Utility functions used in model deployment
├── .gitignore                    # Files and directories to be ignored by Git
├── .pre-commit-config.yaml       # Pre-commit hooks configuration
├── config.py                     # Configuration settings for the project
├── deploy_retrain.py             # Deploy the train_model_workflow with schedule, automatically
├── Dockerfile.app                # Dockerfile
├── environment.yml               # Conda environment configuration file
├── orchestration.py              # Prefect orchestration script for model deployment
├── pyproject.toml                # Project configuration (includes linting and formatting tools)
├── README.md                     # Documentation of the project
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

⚠️**Need to mention**:
Due to dependency version conflict between the latest verion of prefect(3.0.10) and versions of fastapi(>=0.103.2), you need to upgrade your prefect version manually to build your prefect server after building your environment with `requirement.txt`. Use instruction below:
```bash
pip install --upgrade prefect
```


#### Option 1: Using Conda

If you prefer using **conda** for managing environments, follow these steps:

1. **Create and Activate the Environment**

   Create a new conda environment based on the `environment.yml` file:

   ```bash
   conda env create -f environment.yml
   conda activate abandon_env
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

## Train the Model

This project contains two separate workflows:
1. **Training a model**: A Prefect flow that automates the training of a model to predict the age of abalone. The workflow includes steps such as loading the data, processing it (encoding categorical variables), training the model, evaluating the model, and saving the trained model.
2. **Making predictions**: A separate Prefect flow that loads a pre-trained model and processes the data to make predictions on abalone age.

The workflows are separated into different modules and use Prefect's `flow` and `task` objects for automation. Each workflow is built in a reproducible way, meaning the code for training the model and encoding it can be run multiple times with the same outcome, ensuring consistency without requiring a Docker container.

A **Prefect deployment** has also been configured to automatically retrain the model on a daily schedule.

### Code Structure

All core functions for loading data, preprocessing, training, evaluating, saving, and loading models are placed in the `src/modelling/` directory and imported into `orchestration.py` to be used within Prefect tasks and flows. This modular design allows for easy reuse, maintainability, and clarity.

Here’s the breakdown of key modules in the `src/modelling/` folder:
- **`preprocessing.py`**: Contains functions for encoding categorical columns and extracting features (`X`) and targets (`y`) from the dataset.
- **`training.py`**: Provides the functions for loading the dataset and training the model.
- **`predicting.py`**: Handles model predictions and evaluations, including calculating metrics.
- **`utils.py`**: Utility functions for saving and loading pickled model objects, making the process reproducible.

The **`orchestration.py`** file defines all the Prefect tasks and flows by importing these functions from `src/modelling/` and decorating them with Prefect’s `@task` and `@flow` decorators. It contains:
- `train_model_workflow`: A flow that manages the entire process of training the model, from data loading and preprocessing to model saving.
- `batch_predict_workflow`: A flow that handles batch predictions using a pre-trained model.

The **`deploy_retrain.py`** file is used to schedule the `train_model_workflow` for automatic daily retraining, leveraging Prefect’s `CronSchedule` for deployment.

### How to Run the Code

1. **Start the Prefect Server**

   In your terminal, start the Prefect server by running:
   ```bash
   prefect server start
   ```

Make sure to keep this process running while executing workflows or managing deployments.

2. **Train the Model and Make Predictions**

The `orchestration.py` file contains the flows for both training the model and making predictions. You can manually trigger the training or prediction workflows by executing the script in a new terminal, while not closing previous terminal:

```bash
export PREFECT_API_URL=http://localhost:4201/api
python /path/to/orchestration.py
```

This will:
- Load the dataset (`data/abalone.csv`)
- Process the dataset by encoding categorical columns
- Train the model
- Evaluate its performance (RMSE)
- Save the trained model to a file in the specified path (`models/model.pkl`)

It will also:
- Load the saved model for batch prediction
- Generate predictions on the input dataset

⚠️**Need to mention**:
If you encounter the following error message: AttributeError: 'NoneType' object has no attribute 'predict', try to run the command line a second time, and you will resolve the problem.

3. **Deploy the Model for Regular Retraining**

To deploy the model so that it retrains daily, you need to use the `deploy_retrain.py` file. This deployment is configured to retrain the model every day at midnight in the Paris timezone.

Run the following command:

```bash
python /path/to/deploy_retrain.py
```

This creates a deployment that will automatically retrain the model daily at midnight.

4. **Optional: Manually Trigger a Flow Run**

Once the deployment has been set up, you can also manually trigger a flow run using this command:

```bash
prefect deployment run 'Training Model Flow/daily-train-model' --params '{"train_filepath": "/path/to/your/abalone.csv"}'
```

5. **Prefect UI**

You can monitor the status of your flows and deployments through the Prefect UI, accessible via:

```bash
http://0.0.0.0:4200
```

Keep in mind that for scheduled flows to run, the Prefect server must be active.

---
## Using the API

First, enter the file folder of main.py

'''bash
cd /Users/wangchenfei/xhec-mlops-project-student/src/web_service
'''

Second, use instruction below to activate
```bash
uvicorn main:app --reload
```
---

## Using Docker

The project is set up for deployment using **Docker**. You can build and run the Docker container to serve the model with **FastAPI**.

### 1. Build the Docker Image

```bash
docker build -t abalone_age_prediction -f Dockerfile.app .
```

### 2. Run the Docker Container

```bash
docker run -d -p 0.0.0.0:8000:8001 -p 0.0.0.0:4200:4201 abalone_age_prediction
```
Once the container is running:
The FastAPI app can be accessed at http://localhost:8000.
If you have a front-end interface, you can access it at http://localhost:4200.


### 3. Sample Request:
The FastAPI app provides an endpoint to make predictions. You need to use CURL in a new terminal to input data to get prediction. Once the Docker container is running, you can make a `POST` request to the `/predict` endpoint.

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
    "Sex": "M",
    "Length": 0.52,
    "Diameter": 0.35,
    "Height": 0.26,
    "Whole_weight": 0.22,
    "Shucked_weight": 0.24,
    "Viscera_weight": 0.08,
    "Shell_weight": 0.09
}'
```

### Sample Response:

```json
{
  "prediction": 6.708031242815049
}
```

This will return the predicted number of rings for the abalone based on the input features.

---

## Exploratory Data Analysis (EDA)

The project includes an **EDA notebook** that provides insights into the dataset. You can find it in the `eda/eda_notebook.ipynb` file.

---

## Contributors

- **Xianghan Mei** (jazmnm)
- **Chenfei Wang** (ChenfeiWang06)
- **Mingyu Wang** (JANE-WANG-X)
- **Rong Shen** (rongshen799)
- **Xiaohan Ke** (gggg444)

---
