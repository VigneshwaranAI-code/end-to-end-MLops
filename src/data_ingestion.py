import os 
import pandas as pd 
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.Custom_exception import CustomException
from config.paths_config import *
from utils.common_function import read_yaml
import sys


logger = get_logger(__name__)


class DataIngestion:
    def __init__(self,config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_name = self.config["bucket_file_name"]
        self.train_test_ratio = self.config["train_ratio"]

        os.makedirs(RAW_DIR , exist_ok=True)

        logger.info(f"Data ingestion started with {self.bucket_name} and file is {self.file_name}")

    def downlaod_CSV_from_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.file_name)

            blob.download_to_filename(RAW_FILE_PATH)

            logger.info(f'RAW file is sucesfully download to { RAW_FILE_PATH}')

        except Exception as e:
            logger.error(f"Error while Download the CSV file: {str(e)}")
            raise CustomException(f"Failed to download CSV from GCP: {str(e)}", sys)
    def spilt_data(self):
        try:
            logger.info("starting the splitting Process")
            data = pd.read_csv(RAW_FILE_PATH)
            train_data , test_data =train_test_split(data, test_size = 1-self.train_test_ratio, random_state=42)
            
            train_data.to_csv(TRAIN_FILE_PATH)
            test_data.to_csv(TEST_FILE_PATH)

            logger.info(f'Train data saved to {TRAIN_FILE_PATH}')
            logger.info(f'test data saved to {TEST_FILE_PATH}')
        except Exception as e:
            logger.error("Error while splitting/saving train-test files")
            raise CustomException("Failed to split and save train/test data", sys)
        

    def run(self):
        try:
            logger.info("Starting data ingestion process")
            self.downlaod_CSV_from_gcp()
            self.spilt_data()

            logger.info("Data ingestion complete sucesfully")

        except CustomException as ce:
            logger.error(f'CustomException : {str(ce)}')

        finally:
            logger.info("Data ingestion complete")

if __name__ == "__main__":
    config = read_yaml(CONFIG_PATH)
    data_ingestion = DataIngestion(config)
    data_ingestion.run()
        


