import os
import tensorflow as tf
import urllib.request as request
from zipfile import ZipFile
from pathlib import Path
from kidneyDiseaseClassifire.entity.config_entity import BaseModelConfig


class BaseModel:
    def __init__(self, config: BaseModelConfig):
        self.config = config
    
    def download_base_model(self):
        self.model = tf.keras.applications.MobileNetV2(
            input_shape=self.config.image_size,
            include_top=self.config.include_top,
            weights=self.config.weights
        )
        self.save_model(path=self.config.base_model_path, model=self.model)


    @staticmethod
    def save_model(path:Path, model:tf.keras.Model):
        model.save(path)

    @staticmethod
    def update_base_model(
        model,
        classes,
        freeze_all,
        freeze_till,
        learning_rate
         ):

        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif freeze_till:
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        outputs = tf.keras.layers.Dense(classes, activation='softmax')(flatten_in)

        full_model = tf.keras.Model(inputs=model.inputs, outputs=outputs)

        full_model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=['accuracy']
        )
        return full_model
    
    def get_base_model(self):
        self.full_model = self.update_base_model(
            model=self.model,
            classes=self.config.classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.learning_rate
        )

        self.save_model(path=self.config.updated_model_path, model=self.full_model)