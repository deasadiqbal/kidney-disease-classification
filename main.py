from kidneyDiseaseClassifire.pipeline.data_ingestion_stage import DataIngestionStage
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