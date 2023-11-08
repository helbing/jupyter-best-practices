import numpy as np
import pandas as pd
import pytest

from jupyter_best_practices.demo import data_cleansing, handle_distribution_of_time


@pytest.mark.parametrize(
    "data, count",
    [
        (pd.DataFrame.from_dict({"order-status": ["Done", "Done"]}), 1),
        (pd.DataFrame.from_dict({"order-status": ["Done", "Shipping", "Done"]}), 2),
    ],
)
def test_data_cleansing_remove_duplicate_rows(data: pd.DataFrame, count: int):
    result_df = data_cleansing(data)
    assert result_df.shape[0], count


@pytest.mark.parametrize(
    "data, count",
    [
        (pd.DataFrame.from_dict({"order-status": ["Cancelled", "Done"]}), 1),
        (
            pd.DataFrame.from_dict({"order-status": ["Done", "Shipping", "Cancelled"]}),
            2,
        ),
    ],
)
def test_data_cleansing_remove_order_status_is_cancelled(
    data: pd.DataFrame, count: int
):
    result_df = data_cleansing(data)
    assert result_df.shape[0], count


def test_data_cleansing_without_order_status_column_throw_exception():
    data = pd.DataFrame(["other-column"], ["this is text"])

    with pytest.raises(KeyError):
        data_cleansing(data)


def test_handle_distribution_of_time_when_column_not_exists():
    df = pd.DataFrame.from_dict({"order-status": ["Cancelled", "Done"]})

    with pytest.raises(KeyError):
        handle_distribution_of_time(df)


def test_handle_distribution_of_time_success():
    df = pd.DataFrame.from_dict(
        {"purchase-date": ["2022-12-01T12:56:17+00:00", "2022-12-02T13:56:17+00:00"]}
    )

    result = handle_distribution_of_time(df)

    distributionOfTime = np.zeros(24, dtype=int)
    distributionOfTime[12] = 1
    distributionOfTime[13] = 1

    np.testing.assert_array_equal(result, distributionOfTime)
