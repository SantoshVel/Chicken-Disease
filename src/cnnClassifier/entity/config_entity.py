class DataIngestionConfig:
    def __init__(self, source_URL, local_data_file, unzip_dir, root_dir=None):  # Ensure 'root_dir' is included if needed
        self.source_URL = source_URL
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir
        self.root_dir = root_dir  
