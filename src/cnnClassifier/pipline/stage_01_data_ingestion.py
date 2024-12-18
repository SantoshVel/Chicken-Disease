from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger
from pathlib import Path  # Ensure Path is imported

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Define the paths to your config and params files
        config_path = Path(r'C:\Users\Admin\OneDrive\Desktop\Chicken-Disease\config\config.yaml')
        params_path = Path(r'C:\Users\Admin\OneDrive\Desktop\Chicken-Disease\params.yaml')
        
        # Create ConfigurationManager object to manage configurations
        config = ConfigurationManager(config_filepath=config_path, params_filepath=params_path)
        
        # Get the data ingestion configuration from the ConfigurationManager
        data_ingestion_config = config.get_data_ingestion_config()
        
        # Create DataIngestion object and invoke download and extract methods
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Initialize and run the data ingestion pipeline
        obj = DataIngestionTrainingPipeline()
        obj.main()
        
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
        
    except Exception as e:  # Fixed typo 'expext' to 'except'
        logger.exception(e)  # Log the exception with traceback
        raise e  # Reraise the exception to stop execution if critical
