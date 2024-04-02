import io
import pandas as pd
import requests
from pandas import DataFrame

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(**kwargs) -> DataFrame:
    """
    Template for loading data from API
    """
    
    url = 'https://github.com/mik19821/dezoomcamp2024-project/blob/main/data/SPFF-all.csv?raw=True'


    spff_types = {
        'spff':str,
        'znak':str,
        'qsos':pd.Int64Dtype(),
        'dzien':pd.Int64Dtype()
    }


    # df = pd.read_csv(url,sep=',',dtype=spff_types,error_bad_lines=False)
    df = pd.read_csv(url,sep=',',dtype=spff_types)

    return df


@test
def test_output(df) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, 'The output is undefined'
