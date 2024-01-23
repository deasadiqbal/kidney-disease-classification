from kidneyDiseaseClassifire.configs.configurations import ConfigManger
from kidneyDiseaseClassifire.components.base_model import BaseModel
from kidneyDiseaseClassifire import logger

STAGE = "DownloadModelStage"
class DownloadModelStage:
    def __init__(self):
        pass
    def main(self):
        model_config = ConfigManger().get_base_model_config()
        base_model = BaseModel(config=model_config)
        base_model.download_base_model()
        base_model.get_base_model()


if __name__ == "__main__":
    logger.info(f"Running stage: {STAGE}")
    DownloadModelStage().main()
    logger.info(f"Stage completed: {STAGE}")