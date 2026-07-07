"""
RT-DOS Founder Alpha
Version : 0.9.0
"""

from config.settings import APP_NAME, APP_VERSION
from engines.market_data_engine import MarketDataEngine
from engines.technical_engine import TechnicalEngine
from engines.scoring_engine import ScoringEngine
from engines.momentum_engine import MomentumEngine

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
    technical = technical_engine.analyze(result["market_data"])

    scoring_engine = ScoringEngine()
    scored = scoring_engine.calculate(technical)

    momentum_engine = MomentumEngine()
    momentum = momentum_engine.analyze(result["market_data"])

    momentum_map = {item["symbol"]: item for item in momentum}

    print()
    print("=" * 145)
    print("RT-DOS MOMENTUM ENGINE")
    print("=" * 145)

    print(
        f"{'SYMBOL':12}"
        f"{'LTP':12}"
        f"{'EMA20':12}"
        f"{'EMA50':12}"
        f"{'EMA200':12}"
        f"{'TREND SCORE':14}"
        f"{'RSI':10}"
        f"{'MOMENTUM':15}"
    )

    print("-" * 145)

    for item in scored:

        m = momentum_map[item["symbol"]]

        print(
            f"{item['symbol']:12}"
            f"{item['ltp']:12.2f}"
            f"{item['ema20']:12.2f}"
            f"{item['ema50']:12.2f}"
            f"{item['ema200']:12.2f}"
            f"{item['score']:14}"
            f"{m['rsi']:10.2f}"
            f"{m['momentum']:15}"
        )

else:
    print("Market Data Engine Failed")

print()
print("SYSTEM STATUS : READY")
