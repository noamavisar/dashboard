"""Placeholder functions for Interactive Brokers and market data APIs."""

from .schemas import Holding


def get_mock_holdings() -> list[Holding]:
    """Return sample holdings for demo purposes."""
    return [
        Holding(symbol="AAPL", quantity=10, cost_basis=150.0, price=170.0),
        Holding(symbol="MSFT", quantity=5, cost_basis=250.0, price=300.0),
    ]
