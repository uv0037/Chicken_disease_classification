import os
from pathlib import Path  #this will help to recognise that it is windows path and ignore the "/"
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: %(lineno)s')

project_name = "cnnClassifier"

list_of_files=[
    ".github/workflows/.gitkeep",       #used when deploying the app, writing all CI/CD commands (gitkeep is used, when if you commit the code and any file is empty)
    f"src/{project_name}/__init__.py",  #__init__.py is a constructor file which is needed to use that file methods in another file    
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already existing")