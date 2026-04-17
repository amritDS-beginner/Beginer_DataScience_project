from src.mlproject.logger   import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataInjection
import sys

if __name__ == "__main__":
    logging.info("The execution has started")

try:
    data_ingestion = DataInjection()
    data_ingestion.initiate_data_ingestion()

except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e, sys)