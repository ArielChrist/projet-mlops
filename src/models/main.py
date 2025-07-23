import hydra
import joblib
from omegaconf import DictConfig
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import GridSearchCV, cross_val_score
from lightgbm import LGBMRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error
import matplotlib.pyplot

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from preprocessing import DataPreprocessor 


import logging
import logging.config
import yaml
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logger')))
from filters import InfoOnlyFilter

# Charger la configuration YAML

with open(os.path.join(os.path.dirname(__file__),'logging_config.yaml'), 'r') as f:
    config = yaml.safe_load(f)
    logging.config.dictConfig(config)

@hydra.main(config_path="../../configs", config_name="config", version_base=None)
def main(cfg: DictConfig):

    logger = logging.getLogger('app_logger')
    logger.info("Démarrage du programme")

    print("Configuration utilisees")
    print(cfg)

    logger.info("creation de la classe DataPreprocessor")
    logger.info("Chargement des données")
    preprocessing = DataPreprocessor(
        df=(cfg.data.path),
        target_column=cfg.data.target_column,
        exclude_columns=cfg.data.exclude_columns,
        test_size=1 - cfg.train.split_ratio,
        random_state=cfg.train.random_state
    )


    logger.info("Separation des données")
    
    X_train, X_test, y_train, y_test = preprocessing.split_data()

    logger.info("Création du pipeline de prétraitement")
    
    pipeline = preprocessing.create_pipeline(X_train)

    logger.info("Encodage des variables catégorielles et standardisation des données")
    X_train_transform = pipeline.fit_transform(X_train)
    X_test_transform = pipeline.transform(X_test)

    logger.info(f"Donnees X_train_transform de taille {X_train_transform.shape} prete a l'utilisation")

    logger.info("Entraînement du modèle")
    model = cfg.model.name(cfg.model.tol)
    model.fit(X_train_transform, y_train)
    y_pred = model.predict(X_test_transform)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    logger.info("Resultats:")
    logger.info(f"RMSE: {rmse:.2f}")

    logger.info("Enregistrement du modele")
    model_path = os.path.join(cfg.model.save_path, cfg.model.name + '.joblib')
    joblib.dump(model, model_path)
    logger.info(f"Modele enregistre {model_path}")


    pipeline_path = os.path.join(cfg.model.save_path, 'pipeline.joblib')
    joblib.dump(pipeline, pipeline_path)
    logger.info(f"Pipeline enregistre {pipeline_path}")


    logger.warning("fin du programme")


if __name__ == "__main__":
    main()