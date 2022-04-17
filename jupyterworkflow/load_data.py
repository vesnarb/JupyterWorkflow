import os
import pandas as pd
from urllib.request import urlretrieve

URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremond_data(filename = 'Fremond.csv', url = URL, force_download = False):
    """ Download and cache the fremond data

    Parameters
    ------------
    filename: string (optional)
        location to save the data
    url: string (optional)
        web location of the data
    force_download: bool (optional)
        if True, force download the data

    Returns
    ------------
    data: pandas.DataFrame
        The fremond bridge data
    """

    if force_download or not os.path.exists(filename):
        urlretrieve(url, 'Fremond.csv')

    data = pd.read_csv('Fremond.csv', index_col = 'Date')

    try:
        data.index = pd.to_datetime(data.index, format = '%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)


    return data
