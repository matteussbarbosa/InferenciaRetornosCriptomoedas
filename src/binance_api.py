"""
This module defines a function that retrieves historical price time series
data for a financial asset.
"""

from binance.client import Client
import pandas as pd

client = Client()


def historical_price_series(symbol, interval, start, end, oldest_data_first=True):
    """
    Retrieve historical price series for a given asset from Binance.

    Parameters
    ----------
    symbol : str
        Trading pair symbol (e.g., 'BTCUSDT').
    interval : str
        Kline interval (e.g., '1d', '1h').
    start : str
        Start date in 'YYYY-MM-DD' format.
    end : str
        End date in 'YYYY-MM-DD' format.
    oldest_data_first : bool, optional
        Controls whether the DataFrame is ordered in chronological
        (oldest to most recent) or reverse chronological order
        (most recent to oldest). Default is True.

    Returns
    -------
    pandas.DataFrame
        DataFrame indexed by open time, containing
        open, high, low, close and volume data, ordered according to the value
        of the oldest_data_first parameter.
    """
    
    klines = client.get_historical_klines(
        symbol=symbol,
        interval=interval,
        start_str=start,
        end_str=end
    )
    columns = [
        "open_time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "quote_volume",
        "trades",
        "taker_base",
        "taker_quote",
        "ignore"
    ]
    df = pd.DataFrame(klines, columns=columns)
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    df.set_index("open_time", inplace=True)
    df.sort_index(ascending=oldest_data_first, inplace=True)
    df[['open', 'high', 'low', 'close', 'volume']] = (df[['open', 'high', 'low', 'close', 'volume']].astype(float))
    return df