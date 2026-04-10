import os

# Base project directory (one level up from this config package)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

################ Data Ingestion ################
RAW_DIR          = os.path.join(BASE_DIR, "artifacts", "raw")
RAW_FILE_PATH    = os.path.join(RAW_DIR,  "raw.csv")
TRAIN_FILE_PATH  = os.path.join(RAW_DIR,  "train.csv")
TEST_FILE_PATH   = os.path.join(RAW_DIR,  "test.csv")

CONFIG_PATH      = os.path.join(BASE_DIR, "config", "config.yaml")

################ Processed Data ################
PROCESSED_DIR        = os.path.join(BASE_DIR, "artifacts", "processed")
PROCESSED_TRAIN_DATA = os.path.join(PROCESSED_DIR, "processed_train.csv")
PROCESSED_TEST_DATA  = os.path.join(PROCESSED_DIR, "processed_test.csv")

################ Model Output ################
MODEL_DIR         = os.path.join(BASE_DIR, "artifacts", "models")
MODEL_OUTPUT_PATH = os.path.join(MODEL_DIR, "lgbm_model.pkl")