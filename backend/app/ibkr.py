"""Placeholder functions for Interactive Brokers and market data APIs.

This module exposes a ``get_holdings`` function that returns an example
portfolio when the application runs in demo mode.  Supplying IBKR API
credentials and disabling demo mode is reserved for future work.
"""

from __future__ import annotations

import os

from .schemas import Holding


def get_demo_holdings() -> list[Holding]:
    """Return sample holdings for demo purposes."""
    return [
        Holding(symbol="AAPL", quantity=10, cost_basis=150.0, price=170.0),
        Holding(symbol="MSFT", quantity=5, cost_basis=250.0, price=300.0),
        Holding(symbol="GOOG", quantity=2, cost_basis=2000.0, price=2750.0),
    ]


def get_holdings() -> list[Holding]:
    """Return holdings from IBKR or fall back to demo data."""
    if os.getenv("DEMO_MODE", "true").lower() == "true":
        return get_demo_holdings()

    # Placeholder for real IBKR API integration
    raise NotImplementedError("IBKR API integration not implemented yet")
