## Table of contents
* [About project](#about-project)
* [Technologies](#technologies)
* [Software and account requirement](#software-and-account-requirement)
* [Setup](#setup)
* [Project Pipeline](#project-pipeline)
* [Deployment](#Deployment)
<!-- * [License](#license) -->


## About project
This app predicts Insurance premium price based on some data.
The goal of this project is to give people an estimate of how much they need based on
their individual health situation. After that, customers can work with any health
insurance carrier and its plans and perks while keeping the projected cost from our
study in mind. This can assist a person in concentrating on the health side of an
insurance policy rather han the ineffective part.


https://project-insurance.herokuapp.com/


## Technologies
This project is created with below technologies/tools/resorces:
* Python: 3.7
* Machine Learning
* Jupyter Notebook
* HTML/CSS
* Docker
* Git
* CI/CD Pipeline
* Heroku


## Software and Account Requirements
1. [Github Account](https://github.com/)
2. [Heroku Account](https://id.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)


## Setup
Create a conda environment
```
conda create -p venv python==3.7 -y
```

activate conda environment
```
conda activate venv/
```


To install requirement file
```
pip install -r requirements.txt
```

* Add files to git  `git add .` or  `git add <file_name>`    
* To check the git status  `git status`    
* To check all version maintained by git  `git log`    
* To create version/commit all changes by git  `git commit -m "message"`    
* To send version/changes to github  `git push origin main`    
* To check all versions maintained by git `git log`
* To check remote url `git remote -v`
* `Note: To ignore file or folder from git we can write the name of the file/folder in .gitignore folder`

* BUILD DOCKER IMAGE `docker build -t <image_name>:<tagname> .`
* `Note: Image name for docker must be lowercas`
* To list docker image `docker images`
* Run docker image `docker run -p 5000:5000 -e PORT=5000 f8c749e73678`
* To check running container in docker `docker ps`
* To stop docker conatiner `docker stop <container_id>`
* To install ipykernel `pip install ipykernel`
* -e . means install all packages in current directory
* setup.py is required whenever you want to install -e .


## Project Pipeline
1. [Data Ingestion](#1-data-ingestion)
2. [Data Validation](#2-data-validation)
3. [Data Transformation](#3-data-transformation)
4. [Model Training](#4-model-training)
5. [Model Evaluation](#5-model-evaluation)
6. [Model Deployement](#6-model-deployement)


### 1. Data Ingestion: 
* Data ingestion is the process in which unstructured data is extracted from one or multiple sources and then prepared for training machine learning models.

### 2. Data Validation:
* Data validation is an integral part of ML pipeline. It is checking the quality of source data before training a new mode
* It focuses on checking that the statistics of the new data are as expected (e.g. feature distribution, number of categories, etc). 

### 3. Data Transformation 
* Data transformation is the process of converting raw data into a format or structure that would be more suitable for model building.
* It is an imperative step in feature engineering that facilitates discovering insights.

### 4. Model Training
* Model training in machine learning is the process in which a machine learning (ML) algorithm is fed with sufficient training data to learn from.

### 5. Model Evaluation
* Model evaluation is the process of using different evaluation metrics to understand a machine learning model’s performance, as well as its strengths and weaknesses.
* Model evaluation is important to assess the efficacy of a model during initial research phases, and it also plays a role in model monitoring.

### 6. Model Deployement
* Deployment is the method by which we integrate a machine learning model into production environment to make practical business decisions based on data. 


## Deployment
To setup CI/CD pipeline in heroku we need 3 information
```
HEROKU_EMAIL = arkintea@gmail.com
HEROKU_API_KEY = <>
HEROKU_APP_NAME = project-insurance