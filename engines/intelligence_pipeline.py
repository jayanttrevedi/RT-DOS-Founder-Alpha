"""
RT-DOS Intelligence Platform
Module      : Intelligence Pipeline
Version     : 2.0.0
Status      : Production
Architecture: Intelligence Layer
"""

from engines.technical_engine import TechnicalEngine
from engines.scoring_engine import ScoringEngine
from engines.momentum_engine import MomentumEngine
from engines.atr_engine import ATREngine
from engines.volume_engine import VolumeEngine
from engines.relative_strength_engine import RelativeStrengthEngine
from engines.consistency_engine import ConsistencyEngine
from engines.composite_engine import CompositeEngine
from engines.market_regime_engine import MarketRegimeEngine
from engines.institutional_confidence_engine import (
    InstitutionalConfidenceEngine,
)
from engines.probability_engine import ProbabilityEngine


class IntelligencePipeline:

    # ==========================================================
    # Public
    # ==========================================================

    def run(self, market_data):

        # ------------------------------------------------------
        # Technical Analysis
        # ------------------------------------------------------

        technical = TechnicalEngine().analyze(market_data)

        scored = ScoringEngine().calculate(technical)

        momentum = MomentumEngine().analyze(market_data)

        atr = ATREngine().analyze(market_data)

        volume = VolumeEngine().analyze(market_data)

        relative_strength = RelativeStrengthEngine().analyze(market_data)

        # ------------------------------------------------------
        # Consistency Validation
        # ------------------------------------------------------

        consistency = ConsistencyEngine().validate(
            technical,
            momentum,
            atr,
            volume,
            relative_strength,
        )

        if not consistency["success"]:

            raise RuntimeError("Engine Consistency Validation Failed")

        # ------------------------------------------------------
        # Composite Intelligence
        # ------------------------------------------------------

        composite = CompositeEngine().calculate(
            scored,
            momentum,
            atr,
            volume,
            relative_strength,
        )

        # ------------------------------------------------------
        # Market Regime
        # ------------------------------------------------------

        regime = MarketRegimeEngine().analyze(composite)

        # ------------------------------------------------------
        # Institutional Confidence
        # ------------------------------------------------------

        confidence = InstitutionalConfidenceEngine().analyze(regime)

        # ------------------------------------------------------
        # Probability Engine
        # ------------------------------------------------------

        probability = ProbabilityEngine().analyze(confidence)

        return probability
