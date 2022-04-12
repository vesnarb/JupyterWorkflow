from jupyterworkflow.load_data import get_fremond_data
import pandas as pd


def test_data():
    data = get_fremond_data()
    assert all(data.columns == ['Fremont Bridge Total', 'Fremont Bridge East Sidewalk',
           'Fremont Bridge West Sidewalk'])
    assert isinstance(data.index, pd.DatetimeIndex)
