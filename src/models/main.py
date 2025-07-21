import hydra
from omegaconf import DictConfig
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot
from .preprocessing import load_data, preprocess_data, split_data

@hydra.main(config_path="../../configs", config_name="config", version_base=None)
def main(cfg: DictConfig):
    print("Configuration utilisees")
    print(cfg)

    
    df = load_data(cfg.data.path)

    df_clean = preprocess_data(df)

    X_train, X_test, y_train, y_test = split_data(df_clean, cfg.data.target_column, cfg.data.exclude_columns, 1 - cfg.train.split_ratio, cfg.train.random_state)
    
    model_NB = cfg.model.name()
    model_NB.fit(X_train, y_train)
    y_pred_NB = model_NB.predict(X_test)
    rapport_NB = classification_report(y_test, y_pred_NB)
    print(rapport_NB)



if __name__ == "__main__":
    main()