from typing import Type
from crewai_tools import BaseTool
from pydantic import BaseModel, Field
import os
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

# No keys required for crypto data
alpaca_client = CryptoHistoricalDataClient()

class HistoricalMarketDataInput(BaseModel):
    symbol: str = Field(description="The crypto symbol to fetch data for (e.g., 'BTC/USD').")
    start_date: str = Field(description="The start date to fetch data for (YYYY-MM-DD format).")
    interval: str = Field(description="The interval to fetch data for (e.g., '1Day', '1Hour').")

class AlpacaMarketDataTool(BaseTool):
    name: str = "Historical Market Data"
    description: str = """
    Fetches historical market data using Alpaca API for a given stock symbol, start date and candle interval.
    """
    args_schema: Type[BaseModel] = HistoricalMarketDataInput
    
    def _run(self, symbol: str, start_date: str, interval: str) -> str:
        try:
            # Convert start_date string to datetime
            start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
            
            # Map interval string to TimeFrame
            timeframe_map = {
                '1Day': TimeFrame.Day,
                '1Hour': TimeFrame.Hour,
                '1Min': TimeFrame.Minute
            }
            timeframe = timeframe_map.get(interval, TimeFrame.Day)
            
            request_params = CryptoBarsRequest(
                symbol_or_symbols=symbol,
                timeframe=timeframe,
                start=start_datetime
            )
            
            bars = alpaca_client.get_crypto_bars(request_params)
            
            # Format all bars into a readable string
            result = [f"Historical data for {symbol} since {start_date} ({interval} intervals):"]
            for bar in bars[symbol]:
                result.append(
                    f"Time: {bar.timestamp}, "
                    f"Open: {bar.open:.2f}, "
                    f"High: {bar.high:.2f}, "
                    f"Low: {bar.low:.2f}, "
                    f"Close: {bar.close:.2f}, "
                    f"Volume: {bar.volume:.2f}"
                )
            
            return "\n".join(result)
            
        except Exception as e:
            return f"Error fetching market data: {str(e)}"


if __name__ == "__main__":
    tool = AlpacaMarketDataTool()
    print(tool.run(symbol="BTC/USD", start_date="2024-01-01", interval="1Day"))