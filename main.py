from kidneyDiseaseClassifire.pipeline.data_ingestion_stage import DataIngestionStage
from kidneyDiseaseClassifire.pipeline.download_model_stage import DownloadModelStage
from kidneyDiseaseClassifire import logger


STAGE_NAME = "DataIngestionStage"
try:
    logger.info(f"Stage: {STAGE_NAME} started")
    data_ingestion_stage = DataIngestionStage()
    data_ingestion_stage.main()
    logger.info(f"Stage: {STAGE_NAME} completed")   
except Exception as e:
    logger.error(f"Stage: {STAGE_NAME} failed")
    logger.error(e)
    raise e


STAGE_NAME = 'DownloadModelStage'
try:
    logger.info(f"Stage: {STAGE_NAME} started")
    download_model_stage = DownloadModelStage()
    download_model_stage.main()
    logger.info(f"Stage: {STAGE_NAME} completed")
except Exception as e:
    logger.error(f"Stage: {STAGE_NAME} failed")
    logger.error(e)
    raise e