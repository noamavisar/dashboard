import pandas as pd


def sample_price_data() -> pd.DataFrame:
    """Return mock price history for demo purposes."""
    data = {
        "AAPL": [150, 152, 154, 153, 155],
        "MSFT": [300, 305, 310, 308, 312],
        "GOOG": [2700, 2725, 2730, 2740, 2755],
    }
    dates = pd.date_range(end=pd.Timestamp.today(), periods=5)
    return pd.DataFrame(data, index=dates)
