from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

trading_strategy = """
Chart Setup:

Primary timeframe: 4H charts for trade setups
Secondary timeframe: 1H for entry timing
USE BTC/USD

Technical Indicators:

200 EMA (trend direction)
RSI (14 period)
Volume Profile (last 30 days)
MACD (12,26,9)

Entry Rules:

Price must be above/below 200 EMA for long/short
RSI crosses 40/60 line from oversold/overbought
MACD crosses signal line in trend direction
Entry at high-volume nodes from Volume Profile

Risk Management:

Position size: 1-2% account risk per trade
Stop loss: Below/above nearest significant volume node
Take profit: 2:1 minimum risk/reward ratio
Scale out: 50% at 1.5R, move SL to break even

Trade Execution Process:

Confirm BTC trend direction first
Wait for all indicators to align
Enter only during active trading hours (8 AM - 4 PM UTC)
Place limit orders at volume nodes
Exit full position by end of second day if targets not hit

Longs:

Price above 200 EMA
RSI crosses above 40
MACD crosses up
Enter at support volume nodes

Shorts:

Price below 200 EMA
RSI crosses below 60
MACD crosses down
Enter at resistance volume nodes

Definition of Volume Node:
Key Characteristics:

Areas showing above-average volume
Horizontal zones where price spent substantial time
Visible as "bulges" in the Volume Profile indicator

To Identify:

Look for widest parts of Volume Profile
Focus on nodes within last 30 days
Prioritize nodes that caused previous reversals
Most significant nodes have 150%+ of average volume
"""
# Create a knowledge source
trading_strategy_source = StringKnowledgeSource(
    content=trading_strategy, metadata={"trading_strategy": "simple"}
)


