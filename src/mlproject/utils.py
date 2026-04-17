import os
import sys
from src.mlproject.logger   import logging
from src.mlproject.exception import CustomException
from dotenv import load_dotenv
import psycopg2
import pandas as pd


load_dotenv()
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading sql database started")

    try:      
        # Connect to an existing database
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            dbname=db
        )
        df = pd.read_sql_query("Select * from student", conn)
        return df
    except Exception as ex:
        raise CustomException(ex, sys)


