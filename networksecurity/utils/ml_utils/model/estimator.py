from networksecurity.constants.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME
import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkModel:

    def __init__(self, preprocessor, model):
        try:
            self.preprocessor = preprocessor
            self.model = model

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    def predict(self, X):
        try:
            X_transformed = self.preprocessor.transform(X)
            return self.model.predict(X_transformed)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
