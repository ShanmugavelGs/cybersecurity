from cybersecurity.components.data_ingestion import DataIngestion
from cybersecurity.components.data_validation import DataValidation
from cybersecurity.exception.exception import CyberSecurityException
from cybersecurity.logging.logger import logging
from cybersecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from cybersecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Initiate the data validation")
        DataValidationartifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(DataValidationartifact)
    except Exception as e:
           raise CyberSecurityException(e,sys)