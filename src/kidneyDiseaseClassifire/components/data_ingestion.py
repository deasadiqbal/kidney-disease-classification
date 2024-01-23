import os
import zipfile
import gdown
from kidneyDiseaseClassifire import logger
from kidneyDiseaseClassifire.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,
                 config: DataIngestionConfig
                 ):
        self.config = config
    
    def download_data(self) -> str:
        try:
            url = self.config.data_url
            local_data_path = self.config.local_data_path
            # os.makedirs('arifacts/data_ingestion', exist_ok=True)
            logger.info(f"Downloading data from {url} to {local_data_path}")

            dataFile_id = url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+dataFile_id, local_data_path)
            logger.info(f"Data downloaded at {local_data_path}")

        except Exception as e:
            raise e
    
    def unzip_data(self):
        try:
            local_data_path = self.config.local_data_path
            unzip_data_path = self.config.unzip_data_path

            with zipfile.ZipFile(local_data_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_data_path)
            logger.info(f"Data unzipped at {unzip_data_path}")

        except Exception as e:
            raise e
