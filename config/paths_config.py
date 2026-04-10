import os

################ Data ingestion ################

# Base project directory (one level up from this config package)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

RAW_DIR = os.path.join(BASE_DIR, "artifacts", "raw")
RAW_FILE_PATH = os.path.join(RAW_DIR, "raw.csv")
TRAIN_FILE_PATH = os.path.join(RAW_DIR, "train.csv")
TEST_FILE_PATH = os.path.join(RAW_DIR, "test.csv")

# Absolute path to config file so scripts run from any CWD
CONFIG_PATH = os.path.join(BASE_DIR, "config", "config.yaml")


PROCESSED_DIR ="artifacts/processed"
PROCESSED_TRAIN_DATA = os.path.join(PROCESSED_DIR,"processed_train.csv")
PROCESSED_TEST_DATA = os.path.join(PROCESSED_DIR,"processed_test.csv")



########################################Modle Trainign ###################################
MODEL_OUTPUT_PATH = "artifacts/models/lgbm_model.pkl"


