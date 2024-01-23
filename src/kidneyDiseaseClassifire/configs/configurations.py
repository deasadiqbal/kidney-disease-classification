
from kidneyDiseaseClassifire.constants import *
from kidneyDiseaseClassifire.utils.common import *
from kidneyDiseaseClassifire.entity.config_entity import DataIngestionConfig

class ConfigManger:
    def __init__(self,
                 config_filepath = CONFIG_FILEPATH):
        
        self.config = read_yaml(config_filepath)

        create_dirs([self.config.artifacts_roots])

    def get_data_ingestion_confit(self) -> DataIngestionConfig:

        config = self.config.data_ingestion
        create_dirs([config.root_dir])
        
        return DataIngestionConfig(
            root_dir= config.root_dir,
            data_url= config.data_url,
            local_data_path= config.local_data_path,
            unzip_data_path= config.unzip_data_path
        )