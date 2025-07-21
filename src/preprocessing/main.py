import hydra
from omegaconf import DictConfig
import pandas as pd
#from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the DataFrame."""
    # Example preprocessing: fill missing values
    df.fillna(df.mean(), inplace=True)
    return df

@hydra.main(config_path="../../configs", config_name="config", version_base=None)
def main(cfg: DictConfig):
    print("Configuration utilisees")
    print(cfg)

    df = load_data(cfg.data.path)

    print("Preprocessing data...")
    df_clean = preprocess_data(df)
    df_clean.info()

if __name__ == "__main__":
    main()