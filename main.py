"""
RT-DOS Founder Alpha
Version : 1.7.0
"""

from config.settings import APP_NAME, APP_VERSION

from engines.market_data_engine import MarketDataEngine
from engines.technical_engine import TechnicalEngine
from engines.scoring_engine import ScoringEngine
from engines.momentum_engine import MomentumEngine
from engines.atr_engine import ATREngine
from engines.volume_engine import VolumeEngine
from engines.relative_strength_engine import RelativeStrengthEngine
from engines.composite_engine import CompositeEngine
from engines.decision_engine import DecisionEngine
from engines.explainability_engine import ExplainabilityEngine

from reports.report_engine import ReportEngine


def main():

    print("=" * 60)
    print(APP_NAME)
    print(f"Version : {APP_VERSION}")
    print("=" * 60)

    print("Loading Configuration .......... OK")

    market_engine = MarketDataEngine()

    result = market_engine.load()

    if not result["status"]:
        print("Market Data Engine Failed")
        return

    print(f"{result['engine']} ............. OK")
    print(result["message"])
    print(f"Total Symbols : {len(result['watchlist'])}")

    # -----------------------------
    # Intelligence Layer
    # -----------------------------

    technical = TechnicalEngine().analyze(result["market_data"])

    scored = ScoringEngine().calculate(technical)

    momentum = MomentumEngine().analyze(result["market_data"])

    atr = ATREngine().analyze(result["market_data"])

    volume = VolumeEngine().analyze(result["market_data"])

    relative_strength = RelativeStrengthEngine().analyze(result["market_data"])

    # -----------------------------
    # Composite Intelligence
    # -----------------------------

    composite = CompositeEngine().calculate(
        scored, momentum, atr, volume, relative_strength
    )

    # -----------------------------
    # Decision Intelligence
    # -----------------------------

    decisions = DecisionEngine().analyze(composite)

    # -----------------------------
    # Explainable Intelligence
    # -----------------------------

    explanations = ExplainabilityEngine().generate(decisions)

    # -----------------------------
    # Executive Report
    # -----------------------------

    ReportEngine().display(explanations)

    print()
    print("SYSTEM STATUS : READY")


if __name__ == "__main__":
    main()
