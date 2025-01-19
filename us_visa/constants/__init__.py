import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")


DATABASE_NAME = "US_VISA"   ## same name as given in mongodb
COLLECTION_NAME = "visa_data"   ## same name as given in mongodb
MONGODB_URL_KEY = "MONGODB_URL"
PIPELINE_NAME:str = "usvisa"
ARTIFACTS_DIR: str = "artifacts"
FILE_NAME:str = "usvisa.csv"
MODEL_FILE_NAME = "model.pkl"
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

"""
Data Ingeestion related constant start with DATA_INGESTION var name
"""
DATA_INGESTION_COLLECTION_NAME:str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_score"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2