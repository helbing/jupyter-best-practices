"""
This is demo module that support some methods of data handling.
"""

from datetime import datetime

import numpy as np
import pandas as pd


def data_cleansing(df: pd.DataFrame) -> pd.DataFrame:
    """Data cleansing, it will remove duplicate data and remove column of
    order-status's is Cancelled rows.

    Parameters:
        df - uncleaned data

    Returns:
        cleaned data

    Raises:
        KeyError - if the index not found
    """

    # Remove duplicate data
    df = df.drop_duplicates()

    # Remove canceled order
    df = df[df["order-status"] != "Cancelled"]

    return df


def handle_distribution_of_time(
    df: pd.DataFrame,
    column: str = "purchase-date",
    time_format: str = "%Y-%m-%dT%H:%M:%S%z",
) -> np.ndarray[int]:
    """Handle the distribution of time.

    Parameters:
        df - origin data
        column - the column need to be handled
        time_format - time format

    Returns:
        return an numpy array that is the distribution of time

    Raises:
        KeyError - if the index not found
    """

    distributionOfTime = np.zeros(24, dtype=int)

    for _, row in df.iterrows():
        current_datetime = datetime.strptime(row[column], time_format)
        distributionOfTime[current_datetime.hour] += 1

    return distributionOfTime
