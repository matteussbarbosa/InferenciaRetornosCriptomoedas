"""This module defines a function that retrieves logarithmic returns
from an asset."""

import numpy as np
import pandas as pd


def log_return(table: pd.DataFrame) -> pd.DataFrame:
    """
    Retrives logarithmic returns using the column 'close'  (i.e. the close prices)
    from a given pandas.DataFrame.

    Parameters
    ----------
    table : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
        DataFrame, containing the logarithmic returns.
    """
    df = table.copy()
    df['log_return'] = np.log(df['close']).diff()
    return df