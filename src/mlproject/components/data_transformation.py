import os
from mlproject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlproject.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # NOTE:
    # You can add different data transformation techniques such as
    # Scaler, PCA, etc.
    # You can also perform EDA here before passing data to the model.
    # For now, we are only doing train-test split since the data is already clean.

    def train_test_splitting(self):
       
        data = pd.read_csv(self.config.data_path)

        
        train, test = train_test_split(data, test_size=0.25, random_state=42)

        
        train.to_csv(
            os.path.join(self.config.root_dir, "train.csv"),
            index=False
        )
        test.to_csv(
            os.path.join(self.config.root_dir, "test.csv"),
            index=False
        )

        logger.info("Splitted data into training and test sets")
        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")

        print(train.shape)
        print(test.shape)