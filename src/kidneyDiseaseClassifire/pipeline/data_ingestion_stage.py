from kidneyDiseaseClassifire import logger
from kidneyDiseaseClassifire.configs.configurations import ConfigManger
from kidneyDiseaseClassifire.components.data_ingestion import DataIngestion

STAGE_NAME = "DataIngestionStage"
class DataIngestionStage:
    def __init__(self):
        pass
    
    def main(self):
        data_ingestion_config = ConfigManger().get_data_ingestion_confit()
        data_ingestion = DataIngestion(config=data_ingestion_config)

        logger.info('Data Downloading started')
        data_ingestion.download_data()
        logger.info('Data Downloading completed')

        logger.info('Data Unzipping started')
        data_ingestion.unzip_data()
        logger.info('Data Unzipping completed')

if __name__ == "__main__":
    data_ingestion_stage = DataIngestionStage()
    data_ingestion_stage.main()
