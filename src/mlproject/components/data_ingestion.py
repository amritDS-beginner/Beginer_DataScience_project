import os
import sys
from src.mlproject.logger   import logging
from src.mlproject.exception import CustomException
import pandas as pd
from dataclasses import dataclass
from src.mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split


@dataclass
class DataingestionConfig:
    train_data_path:str=os.path.join("artifacts", "train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts", "raw_data.csv")


class DataInjection:
    def __init__(self):
        self.injection_config = DataingestionConfig()
        
    def initiate_data_ingestion(self):

        try:
            df = read_sql_data()
            logging.info("Reading completed data from database")

            os.makedirs("artifacts", exist_ok=True)
            df.to_csv(self.injection_config.raw_data_path, header=True, index=False)

            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
            train_data.to_csv(self.injection_config.train_data_path, index=False, header=True)
            test_data.to_csv(self.injection_config.test_data_path, index=False, header=True)
            
            return (
                self.injection_config.train_data_path,
                self.injection_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
