"""
RT-DOS Founder Alpha
Version : 0.8.0
"""

from config.settings import APP_NAME, APP_VERSION
from engines.market_data_engine import MarketDataEngine
from engines.technical_engine import TechnicalEngine
from engines.scoring_engine import ScoringEngine

print("=" * 60)
print(APP_NAME)
print(f"Version : {APP_VERSION}")
print("=" * 60)

print("Loading Configuration .......... OK")

market_engine = MarketDataEngine()

result = market_engine.load()

if result["status"]:

    print(f"{result['engine']} ............. OK")
    print(result["message"])
    print(f"Total Symbols : {len(result['watchlist'])}")

    technical_engine = TechnicalEngine()
    analysis = technical_engine.analyze(result["market_data"])

    scoring_engine = ScoringEngine()
    scored = scoring_engine.calculate(analysis)

    print()
    print("=" * 125)
    print("RT-DOS SCORING ENGINE")
    print("=" * 125)

    print(
        f"{'SYMBOL':12}"
        f"{'LTP':12}"
        f"{'EMA20':12}"
        f"{'EMA50':12}"
        f"{'EMA200':12}"
        f"{'SCORE':8}"
        f"{'TREND':20}"
    )

    print("-" * 125)

    for item in scored:

        print(
            f"{item['symbol']:12}"
            f"{item['ltp']:12.2f}"
            f"{item['ema20']:12.2f}"
            f"{item['ema50']:12.2f}"
            f"{item['ema200']:12.2f}"
            f"{item['score']:8}"
            f"{item['trend']:20}"
        )

else:
    print("Market Data Engine Failed")

print()
print("SYSTEM STATUS : READY")
