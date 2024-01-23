import os
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    data_url: str
    local_data_path: Path
    unzip_data_path: Path


@dataclass(frozen=True)
class BaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_model_path: Path
    image_size: list
    learning_rate: float
    include_top: bool
    weights: str
    classes: int