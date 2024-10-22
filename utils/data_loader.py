import pandas as pd


def load_dataframes():
    """
    Load two datasets from parquet files into pandas DataFrames.

    Returns:
        tuple: A tuple containing two pandas DataFrames:
            - df (pd.DataFrame): The first dataset loaded from 'path_to_first_dataset.parquet'.
            - df2 (pd.DataFrame): The second dataset loaded from 'path_to_second_dataset.parquet'.

    Raises:
        FileNotFoundError: If either of the parquet files is not found.
        pd.errors.EmptyDataError: If either of the parquet files is empty.
    """
    df = pd.read_parquet("path_to_first_dataset.parquet")
    df2 = pd.read_parquet("path_to_second_dataset.parquet")
    return df, df2
