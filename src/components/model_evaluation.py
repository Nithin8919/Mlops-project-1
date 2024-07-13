import pandas as pd
import numpy as np
from src.logger.app_logging import logging
from src.exception.exception import customexception
import pickle 
import mlflow
import mlflow.sklearn
from sklearn.metrics import mean_squared_error,mean_absolute_error
from urllib.parse import urlparse
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path # to write the path without any issues like mac os and windows / \

@dataclass
class ModelEvaluationConfig:
    pass

class ModelEvaluation:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)