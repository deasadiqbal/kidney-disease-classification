
from kidneyDiseaseClassifire.constants import *
from kidneyDiseaseClassifire.utils.common import *
from kidneyDiseaseClassifire.entity.config_entity import (DataIngestionConfig,
                                                          BaseModelConfig)


class ConfigManger:
    def __init__(self,
                 config_filepath = CONFIG_FILEPATH,
                 params = PARAMS_FILEPATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params)

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
    
    def get_base_model_config(self) -> BaseModelConfig:
        config = self.config.base_model

        create_dirs([config.root_dir])

        return BaseModelConfig(
            root_dir= config.root_dir,
            base_model_path= config.base_model_path,
            updated_model_path= config.updated_model_path,
            image_size= self.params.IMAGE_SIZE,
            learning_rate= self.params.LEARNING_RATE,
            include_top= self.params.INCLUDE_TOP,
            classes= self.params.CLASSES,
            weights= self.params.WEIGHTS
        )