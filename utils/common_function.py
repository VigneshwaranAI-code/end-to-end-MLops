import os
import sys
import yaml
from src.logger import get_logger
from src.Custom_exception import CustomException
import pandas as pd

logger = get_logger(__name__)


def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found in given path")

        with open(file_path, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Successfully read YAML file")
            return config

    except Exception as e:
        logger.error("Error while reading YAML file")
        raise CustomException("Failed to read YAML file", sys)
 
def load_data(path):
    try:
        logger.info("loading the data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f'error of loading the data {e}')
        raise CustomException("Failed to load data", e)
    