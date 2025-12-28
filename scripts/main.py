"""This module computes a confidence interval for the mean of returns."""

import numpy as np
import sys
import os
from scipy.stats import t

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.binance_api import historical_price_series
from src.log_returns import log_return


CURRENCY = 'BTCUSDT'
START_TIME = '2024-01-01 00:00:00' 
END_TIME = '2025-01-01 00:00:00'

df = historical_price_series(CURRENCY, '1h', START_TIME, END_TIME)
df_returns = log_return(df)
returns = df_returns['log_return'].dropna()


# This section calculates the sample parameters.

sample_mean = returns.mean()
sample_std = returns.std(ddof=1)
standard_error = sample_std / np.sqrt(returns.shape[0])

# This section calculates the confidence interval for a 5% signficance level.

alpha = 0.05
alpha2 = alpha / 2
degrees_of_freedom = returns.shape[0]-1
t_critical = t.ppf(1 - alpha2, df=degrees_of_freedom)

lower_ci_limit = sample_mean-(t_critical * standard_error)
upper_ci_limit = sample_mean+(t_critical * standard_error)

print(f'We are 95% confident tha the mean is between {lower_ci_limit} and {upper_ci_limit}.')