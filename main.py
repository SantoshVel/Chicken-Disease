from cnnClassifier import logger
from cnnClassifier.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# Other imports
import os
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from pathlib import Path

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:  # Fixed the typo here from 'expext' to 'except'
    logger.exception(e)
    raise e