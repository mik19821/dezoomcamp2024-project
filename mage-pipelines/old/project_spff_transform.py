import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent blockdate_column
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    data['dzien'].isna().sum()
    # Specify your transformation logic here
    data['znak'] = data['znak'].str.upper()

    date_column = 'dzien'
    try:
        data['dzien'] = pd.to_datetime(data['dzien'], format='%Y%m%d')
    except ValueError:
        data[date_column] = pd.to_datetime(data[date_column], errors='coerce')
        data[date_column].fillna(pd.Timestamp('1900-01-01'), inplace=True)
        wrong_dates = data[pd.to_datetime(data[date_column], errors='coerce').isnull()]
        if not wrong_dates.empty:
            print("\nRows with wrong date format:")
            print(wrong_dates)

    return data

# @test
# def test_output(output, *args) -> None:

#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
