from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml,create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_filepath, params_filepath):
        # Load YAML files as dictionaries
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Create necessary directories
        create_directories([self.config["artifacts_root"]])
    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Access 'data_ingestion' dictionary correctly
        config = self.config["data_ingestion"]
        create_directories([config["root_dir"]])

        # Create and return DataIngestionConfig instance
        return DataIngestionConfig(
            root_dir=config["root_dir"],
            source_URL=config["source_URL"],
            local_data_file=config["local_data_file"],
            unzip_dir=config["unzip_dir"]
        )
        return data_ingestion_config