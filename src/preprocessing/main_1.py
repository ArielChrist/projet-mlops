import pandas as pd
import numpy as np
from category_encoders import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def impute_outliers(data, colname): 
    q1 = np.percentile(data[colname], 25)
    q3 = np.percentile(data[colname], 75) 

    lower_bound = q1 - 1.5*(q3 - q1)
    upper_bound = q3 + 1.5*(q3 - q1)

    data.loc[(data[colname] <= lower_bound), colname] = lower_bound
    data.loc[(data[colname] >= upper_bound), colname] = upper_bound


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the DataFrame."""
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day

    for colname in df.select_dtypes('number').columns:
        impute_outliers(df, colname)

    


    df = OneHotEncoder(cols=['city', 'street'], drop_invariant=True).fit_transform(df)
    

    df = StandardScaler().fit_transform(df.select_dtypes(include=['float64', 'int64']))


    return df_clean 


def split_data(df: pd.DataFrame, target_column:str, exclude_columns: list, test_size: float, random_state: int) -> list:
    """
    Divise les données en ensembles d'entraînement et de test.

    Returns:
    --------
    X_train, X_test, y_train, y_test : tuple
        Données divisées en ensembles d'entraînement et de test.
    """
    y = df[target_column]
    X = df.drop([target_column] + exclude_columns, axis='columns')

    X_train, X_test, y_train, y_test = train_test_split(
                                X, 
                                y, 
                                test_size=test_size, 
                                random_state=random_state
                        )
    return X_train, X_test, y_train, y_test

