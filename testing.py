from src.logger import get_logger
from src.Custom_exception import customeException
import sys
logger=get_logger(__name__)

def divid_number(a,b):
    try:
        result = a/b
        logger.info("dividing two number")
        return logger
    except Exception as e:
        logger.error("error occured")
        raise customeException("custom error Zero",sys)

if __name__ == "__main__":
    try:
        logger.info("starting main program")
        divid_number(10,1)
    except customeException as ce:
        logger.error(str(ce))