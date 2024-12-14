from dataclasses import dataclass, field
from typing import Dict, Optional
import pandas as pd

@dataclass
class MarketState:
    """Global state for market data."""
    symbol: str = ''
    timeframe: str = ''
    current_price: float = 0.0
    historical_data: Optional[pd.DataFrame] = None
    indicators: Dict = field(default_factory=dict)
    last_updated: Optional[str] = None

    def update_price(self, price: float) -> None:
        """Update the current price."""
        self.current_price = price

    def update_historical_data(self, data: pd.DataFrame) -> None:
        """Update historical price data."""
        self.historical_data = data

    def add_indicator(self, name: str, value: any) -> None:
        """Add or update a technical indicator."""
        self.indicators[name] = value

    def get_indicator(self, name: str) -> any:
        """Get a technical indicator value."""
        return self.indicators.get(name)

# Global market state instance
market_state = MarketState()
