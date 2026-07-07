"""
RT-DOS Founder Alpha
"""

from config.settings import APP_NAME, APP_VERSION
from engines.market_data_engine import MarketDataEngine

print("=" * 60)
print(APP_NAME)
print(f"Version : {APP_VERSION}")
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
