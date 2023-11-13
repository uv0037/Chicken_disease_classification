import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file and returns

    Args:
        path_to_yaml(str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content =  yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):            #this is used to make the directories in the artifacts folder i.e.data ingestion, model, etc
    """"creaate list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
        
def save_json(path: Path, data:dict):           #this json file is created to save the accuracy and loss after evalaution model.
    """ save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """ load json files data
    Args: 
        path (Path): path to json file
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content=json.load(f)

    logger.info(f"json file loaded successfully from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path) -> ConfigBox:
    """ save binary file
    Args: 
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> ConfigBox:
    """ load binary data
    Args:
        path (Path): path to binary file
    Returns:
        data (Any): object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> ConfigBox:
    """ get size in Kb
    Args: 
        path (Path): path of the file
    Returns:
        str: size in Kb
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

def decodeImage (imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def enodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64dencode(f.read())