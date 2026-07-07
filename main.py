"""
RT-DOS Founder Alpha
Version 0.1.0
"""

from engines.market_data_engine import MarketDataEngine
from config.settings import PROJECT_NAME, VERSION

print("=" * 60)
print(PROJECT_NAME)
print(f"Version : {VERSION}")
print("=" * 60)

print("Loading Configuration .......... OK")
engine = MarketDataEngine()

result = engine.load()

if result["status"]:
    print(f'{result["engine"]} ............. OK')
    print(result["message"])
    print(f'Total Symbols : {len(result["watchlist"])}')
else:
    print("Market Data Engine Failed")

print()
print("SYSTEM STATUS : READY")
