from cybersecurity.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME

import os
import sys

from cybersecurity.exception.exception import CyberSecurityException
from cybersecurity.logging.logger import logging

class CyberModel:
    def __init__(self,preprocessor,model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise CyberSecurityException(e,sys)
    
    def predict(self,x):
        try:
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise CyberSecurityException(e,sys)