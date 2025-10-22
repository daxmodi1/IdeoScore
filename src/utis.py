import os
import sys
import pandas as pd
import numpy as np
import dill

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.exeption import CustomException
from src.logger import logging 
def save_object(dir_path, obj):
    try:
        dir_path = os.path.dirname(dir_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(dir_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
        logging.info("Exception occurred in save_object function")
