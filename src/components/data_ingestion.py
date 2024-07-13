import sys
import os
import pandas as pd
import numpy as np
from src.logger.app_logging import logging
from src.exception.exception import customexception
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path  # to write the path without any issues like macOS and Windows / \

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", 'train.csv')
    test_data_path: str = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            data = pd.read_csv("/Users/nitin/Documents/Mlops_gems_pro/mlops1/data/train.csv")
            logging.info("Reading dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Saved the raw dataset in artifacts folder")
            
            logging.info("Performing train-test split")
            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("Train-test split completed")
            
            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            
            logging.info("Data ingestion part completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.error("Data ingestion failed")
            raise customexception(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
