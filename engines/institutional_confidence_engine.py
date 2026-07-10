"""
RT-DOS Intelligence Platform
Module      : Institutional Confidence Engine
Version     : 1.0.0
Status      : Production
Architecture: Intelligence Layer
"""

from typing import Dict, List


class InstitutionalConfidenceEngine:
    """
    Calculates the RT-DOS Institutional Confidence Index (ICI).

    Version 1 is intentionally transparent and deterministic.

    Future versions may incorporate:
        - AI weighting
        - Back-tested coefficients
        - Market breadth
        - India VIX
        - Sector leadership
    """

    # ==========================================================
    # Public
    # ==========================================================

    def analyze(
        self,
        regime_data: List[Dict],
    ) -> List[Dict]:

        if not regime_data:
            return []

        output = []

        for asset in regime_data:

            confidence = self._calculate(asset)

            asset = asset.copy()

            asset["institutional_confidence"] = confidence
            asset["confidence_grade"] = self._grade(confidence)
            asset["signal_strength"] = self._signal_strength(confidence)
            asset["trade_quality"] = self._trade_quality(confidence)

            output.append(asset)

        return output

    # ==========================================================
    # Private
    # ==========================================================

    def _calculate(
        self,
        asset: Dict,
    ) -> int:

        score = asset.get("score", 0)

        regime = asset.get("market_regime", "")

        regime_bonus = {
            "Strong Bull Trend": 12,
            "Bull Trend": 8,
            "Accumulation": 5,
            "Breakout Watch": 3,
            "Sideways": 0,
            "Distribution": -5,
            "Bear Trend": -10,
            "High Risk": -15,
        }.get(regime, 0)

        confidence = score + regime_bonus

        confidence = max(0, min(100, int(confidence)))

        return confidence

    # ----------------------------------------------------------

    def _grade(
        self,
        confidence: int,
    ) -> str:

        if confidence >= 90:
            return "A+"

        if confidence >= 80:
            return "A"

        if confidence >= 70:
            return "B"

        if confidence >= 60:
            return "C"

        if confidence >= 50:
            return "D"

        return "E"

    # ----------------------------------------------------------

    def _signal_strength(
        self,
        confidence: int,
    ) -> str:

        if confidence >= 85:
            return "VERY HIGH"

        if confidence >= 70:
            return "HIGH"

        if confidence >= 55:
            return "MODERATE"

        if confidence >= 40:
            return "LOW"

        return "VERY LOW"

    # ----------------------------------------------------------

    def _trade_quality(
        self,
        confidence: int,
    ) -> str:

        if confidence >= 90:
            return "INSTITUTIONAL"

        if confidence >= 75:
            return "HIGH"

        if confidence >= 60:
            return "GOOD"

        if confidence >= 45:
            return "AVERAGE"

        return "POOR"
