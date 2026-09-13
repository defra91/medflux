# src/db.py

import pandas as pd
from .config import ORIGINAL_DB_PATH, DESTINATION_DB_PATH

def load_db() -> pd.DataFrame:
    """
    Load the database from the Excel file.

    Returns:
        pd.DataFrame: The loaded database as a pandas DataFrame.
    """
    df = pd.read_excel(ORIGINAL_DB_PATH)
    return df

def save_db(df: pd.DataFrame) -> None:
    """
    Save the database to the Excel file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
    """
    df.to_excel(DESTINATION_DB_PATH, index=False)