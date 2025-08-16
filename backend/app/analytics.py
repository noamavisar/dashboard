import numpy as np
import pandas as pd
from .data import sample_price_data


def compute_metrics() -> dict:
    """Calculate basic portfolio risk metrics."""
    prices = sample_price_data()
    returns = prices.pct_change().dropna()
    mean_returns = returns.mean()
    volatility = returns.std()
    sharpe = (mean_returns.mean() / volatility.mean()) * np.sqrt(252)
    corr = returns.corr()
    return {
        "sharpe": float(sharpe),
        "volatility": float(volatility.mean()),
        "tickers": list(corr.columns),
        "correlation": corr.values.tolist(),
    }
