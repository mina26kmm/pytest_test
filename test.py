import pandas as pd
from pipeline import clean_data, transform_data, run_pipeline

def test_clean_data():
    df = pd.DataFrame({"value": [1, None, 3]})
    cleaned = clean_data(df)
    assert len(cleaned) == 2
    assert cleaned["value"].tolist() == [1, 3]

def test_transform_data():
    df = pd.DataFrame({"value": [2]})
    transformed = transform_data(df)
    assert "double" in transformed.columns
    assert transformed.loc[0, "double"] == 4

def test_run_pipeline_end_to_end():
    df = pd.DataFrame({"value": [1, None, 2]})
    result = run_pipeline(df)
    assert result["double"].tolist() == [2, 4]