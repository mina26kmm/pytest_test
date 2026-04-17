import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with missing 'value'."""
    return df.dropna(subset=["value"])

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Add a new column that doubles 'value'."""
    df = df.copy()
    df["double"] = df["value"] * 2
    return df

def run_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = clean_data(df)
    transformed = transform_data(cleaned)
    
