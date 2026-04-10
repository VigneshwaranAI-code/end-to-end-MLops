import logging
import os 
from datetime import datetime

LOGs_DIR ="logs"
os.makedirs(LOGs_DIR,exist_ok=True)

LOG_FILE = os.path.join(LOGs_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOG_FILE, #folder to log files 
    filemode='a', #a is append w is writen r - read only 
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def get_logger(name):  # Function to create and return a logger
    logger = logging.getLogger(name)  # Get a logger object with the given name
    logger.setLevel(logging.INFO)  # Set logging level to INFO (ignore DEBUG messages)
    return logger  # Return the configured logger




