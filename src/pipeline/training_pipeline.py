import os
import sys

# Add the root directory of your project to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.logger.logging import logging
from src.exception.exception import customexception
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

if __name__ == "__main__":
    try:
        logging.info("Starting data ingestion process.")
        print("Starting data ingestion process.")
        obj = DataIngestion()

        train_data_path, test_data_path = obj.initiate_data_ingestion()
        logging.info(f"Data ingestion completed. Train data path: {train_data_path}, Test data path: {test_data_path}")
        print(f"Data ingestion completed. Train data path: {train_data_path}, Test data path: {test_data_path}")

        logging.info("Starting data transformation process.")
        print("Starting data transformation process.")
        data_transformation = DataTransformation()
        train_arr, test_arr = data_transformation.initialize_data_transformation(train_data_path, test_data_path)
        logging.info("Data transformation completed.")
        print("Data transformation completed.")

        logging.info("Starting model training process.")
        print("Starting model training process.")
        model_trainer_obj = ModelTrainer()
        model_trainer_obj.initate_model_training(train_arr, test_arr)
        logging.info("Model training completed.")
        print("Model training completed.")

        logging.info("Starting model evaluation process.")
        print("Starting model evaluation process.")
        model_eval_obj = ModelEvaluation()
        model_eval_obj.initiate_model_evaluation(train_arr, test_arr)
        logging.info("Model evaluation completed.")
        print("Model evaluation completed.")

    except Exception as e:
        logging.error("Exception occurred in the main execution block.")
        logging.exception(e)
        print("Exception occurred in the main execution block.")
        print(e)
