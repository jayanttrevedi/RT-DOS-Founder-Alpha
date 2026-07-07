"""
RT-DOS Founder Alpha
Version : 1.2.0
"""

from config.settings import APP_NAME, APP_VERSION

from engines.market_data_engine import MarketDataEngine
from engines.technical_engine import TechnicalEngine
from engines.scoring_engine import ScoringEngine
from engines.momentum_engine import MomentumEngine
from engines.atr_engine import ATREngine
from engines.volume_engine import VolumeEngine

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

    atr_engine = ATREngine()
    atr_data = atr_engine.analyze(result["market_data"])

    volume_engine = VolumeEngine()
    volume_data = volume_engine.analyze(result["market_data"])

    momentum_map = {item["symbol"]: item for item in momentum}

    atr_map = {item["symbol"]: item for item in atr_data}

    volume_map = {item["symbol"]: item for item in volume_data}

    print()
    print("=" * 210)
    print("RT-DOS FOUNDER ALPHA - INTELLIGENCE ENGINE")
    print("=" * 210)

    print(
        f"{'SYMBOL':12}"
        f"{'LTP':12}"
        f"{'EMA20':12}"
        f"{'EMA50':12}"
        f"{'EMA200':12}"
        f"{'TREND':8}"
        f"{'RSI':10}"
        f"{'ATR':12}"
        f"{'VOL':12}"
        f"{'VOL RATIO':12}"
        f"{'VOLUME':15}"
        f"{'MOMENTUM':15}"
    )

    print("-" * 210)

    for item in scored:

        m = momentum_map[item["symbol"]]
        a = atr_map[item["symbol"]]
        v = volume_map[item["symbol"]]

        print(
            f"{item['symbol']:12}"
            f"{item['ltp']:12.2f}"
            f"{item['ema20']:12.2f}"
            f"{item['ema50']:12.2f}"
            f"{item['ema200']:12.2f}"
            f"{item['score']:8}"
            f"{m['rsi']:10.2f}"
            f"{a['atr']:12.2f}"
            f"{v['current_volume']:12}"
            f"{v['volume_ratio']:12.2f}"
            f"{v['volume_strength']:15}"
            f"{m['momentum']:15}"
        )

else:
    print("Market Data Engine Failed")

print()
print("SYSTEM STATUS : READY")
