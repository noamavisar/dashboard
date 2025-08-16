import numpy as np
from pypfopt import EfficientFrontier, expected_returns, risk_models
from .data import sample_price_data


def efficient_frontier_points(n_points: int = 20) -> list[dict]:
    """Approximate efficient frontier using PyPortfolioOpt."""
    prices = sample_price_data()
    mu = expected_returns.mean_historical_return(prices)
    S = risk_models.sample_cov(prices)
    ef_min = EfficientFrontier(mu, S, solver="SCS")
    ef_min.min_volatility()
    ret_min, vol_min, _ = ef_min.portfolio_performance()
    ef_max = EfficientFrontier(mu, S, solver="SCS")
    ef_max.max_sharpe()
    ret_max, vol_max, _ = ef_max.portfolio_performance()
    risks = np.linspace(vol_min, vol_max, n_points)
    rets = np.linspace(ret_min, ret_max, n_points)
    return [
        {"risk": float(r), "return": float(ret)}
        for r, ret in zip(risks, rets)
    ]
