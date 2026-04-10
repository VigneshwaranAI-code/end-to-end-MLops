from src.data_ingestion import DataIngestion 
from src.model_training import ModelTraining
from src.data_processing import DataProcessor
from utils.common_function import read_yaml
from config.paths_config import *


if __name__ == "__main__":
    
     #Data Ingestion 
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()

    ## 2. Data processing
    processor = DataProcessor(TRAIN_FILE_PATH , TEST_FILE_PATH , PROCESSED_DIR,CONFIG_PATH)
    processor.process()

    ###3 model Training 

    trainer = ModelTraining(PROCESSED_TRAIN_DATA,PROCESSED_TEST_DATA,MODEL_OUTPUT_PATH)
    trainer.run()



