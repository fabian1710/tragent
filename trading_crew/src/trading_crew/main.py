import logging
from typing import List, Optional
from trading_crew.crew import TradingCrew
from trading_crew.state import market_state

log = logging.getLogger(__name__)

def run_trading_crew(
    symbol: str,
    timeframe: str = '1h',
    test: bool = False,
    credentials_path: Optional[str] = None,
) -> None:
    """Run the trading crew for a specific symbol and timeframe.

    Args:
        symbol: Trading pair symbol (e.g., 'BTC/USDT')
        timeframe: Candlestick timeframe (default: '1h')
        test: Whether to run in test mode
        credentials_path: Path to credentials file
    """
    # Initialize market state
    market_state.symbol = symbol
    market_state.timeframe = timeframe

    crew = TradingCrew(test=test, credentials_path=credentials_path)
    crew.run()

def main():
    """Main entry point for the trading crew application."""
    import argparse

    parser = argparse.ArgumentParser(description='Run the trading crew')
    parser.add_argument('--symbol', type=str, required=True, help='Trading pair symbol')
    parser.add_argument('--timeframe', type=str, default='1h', help='Candlestick timeframe')
    parser.add_argument('--test', action='store_true', help='Run in test mode')
    parser.add_argument('--credentials', type=str, help='Path to credentials file')

    args = parser.parse_args()

    run_trading_crew(
        symbol=args.symbol,
        timeframe=args.timeframe,
        test=args.test,
        credentials_path=args.credentials,
    )

if __name__ == '__main__':
    main()
