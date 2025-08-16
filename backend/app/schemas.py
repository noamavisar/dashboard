from pydantic import BaseModel, Field


class Holding(BaseModel):
    symbol: str
    quantity: int
    cost_basis: float
    price: float

    class Config:
        orm_mode = True


class Analytics(BaseModel):
    sharpe: float
    volatility: float
    tickers: list[str]
    correlation: list[list[float]]


class FrontierPoint(BaseModel):
    risk: float
    expected_return: float = Field(..., alias="return")

    class Config:
        allow_population_by_field_name = True
