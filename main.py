from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import Datatransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

#Example for data ingestion
# if __name__=="__main__":
#     try:
#         trainingpipelineconfig=TrainingPipelineConfig()
#         dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
#         data_ingestion=DataIngestion(dataingestionconfig)
#         logging.info("Initiate the data ingestion")
#         dataingestionartifact=data_ingestion.initiate_data_ingestion()
#         print(dataingestionartifact)

#     except Exception as e:
#         raise NetworkSecurityException(e,sys)

#Example for data validation
# if __name__=="__main__":
#     try:
#         trainingpipelineconfig=TrainingPipelineConfig()
#         dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
#         data_ingestion=DataIngestion(dataingestionconfig)
#         logging.info("Initiate the data ingestion")
#         dataingestionartifact=data_ingestion.initiate_data_ingestion()
#         logging.info("Data ingestion Completed!")
#         data_validation_config=DataValidationConfig(trainingpipelineconfig)
#         data_validation=DataValidation(dataingestionartifact,data_validation_config)
#         logging.info("Initiate Data Validation")
#         data_validation_artifact=data_validation.initiate_data_validation()
#         logging.info("Data Validation Completed!")
#         print(data_validation_artifact)

#     except Exception as e:
#         raise NetworkSecurityException(e,sys)

#Example for data transformation
# if __name__=="__main__":
#     try:
#         trainingpipelineconfig=TrainingPipelineConfig()
#         dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
#         data_ingestion=DataIngestion(dataingestionconfig)
#         logging.info("Initiate the data ingestion")
#         dataingestionartifact=data_ingestion.initiate_data_ingestion()
#         logging.info("Data ingestion Completed!")
#         data_validation_config=DataValidationConfig(trainingpipelineconfig)
#         data_validation=DataValidation(dataingestionartifact,data_validation_config)
#         logging.info("Initiate Data Validation")
#         data_validation_artifact=data_validation.initiate_data_validation()
#         logging.info("Data Validation Completed!")
#         data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
#         data_transformation=Datatransformation(data_validation_artifact,data_transformation_config)
#         logging.info("Initiate Data Transformation")
#         data_transformation_artifacts=data_transformation.initiate_data_transformation()
#         logging.info("Data Transformation completed!")
#         print(data_transformation_artifacts)
#     except Exception as e:
#         raise NetworkSecurityException(e,sys)

