"""
RT-DOS Founder Alpha
"""

from config.settings import APP_NAME, APP_VERSION
from engines.market_data_engine import MarketDataEngine
from engines.technical_engine import TechnicalEngine

print("=" * 60)
print(APP_NAME)
print(f"Version : {APP_VERSION}")
print("=" * 60)

print("Loading Configuration .......... OK")

market_engine = MarketDataEngine()
result = market_engine.load()

if result["status"]:

    print(f'{result["engine"]} ............. OK')
    print(result["message"])
    print(f"Total Symbols : {len(result['watchlist'])}")

    technical_engine = TechnicalEngine()
    analysis = technical_engine.analyze(result["market_data"])

    print("\n")
    print("=" * 72)
    print("TECHNICAL ANALYSIS")
    print("=" * 72)

    print(f"{'SYMBOL':12}" f"{'LTP':12}" f"{'EMA20':12}" f"{'EMA50':12}")

    print("-" * 48)

    for item in analysis:

        print(
            f"{item['symbol']:12}"
            f"{item['ltp']:12.2f}"
            f"{item['ema20']:12.2f}"
            f"{item['ema50']:12.2f}"
        )

else:
    print("Market Data Engine Failed")

print()
print("SYSTEM STATUS : READY")
