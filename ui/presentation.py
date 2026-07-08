"""
RT-DOS Intelligence Platform
Module      : Presentation Engine
Version     : 3.0.0
Status      : Production Candidate
Architecture: Workspace Framework
"""

from datetime import datetime


class PresentationEngine:
    """
    Converts Decision Engine output into presentation-ready data
    for the RT-DOS Workspace.
    """

    def build(self, decisions):

        if not decisions:
            return self._empty()

        ranked = sorted(
            decisions,
            key=lambda x: x["score"],
            reverse=True,
        )

        total_assets = len(ranked)

        strong_buy = sum(1 for item in ranked if item["decision"] == "STRONG BUY")

        buy = sum(1 for item in ranked if item["decision"] == "BUY")

        watch = sum(1 for item in ranked if item["decision"] == "WATCH")

        hold = sum(1 for item in ranked if item["decision"] == "HOLD")

        avoid = sum(1 for item in ranked if item["decision"] == "AVOID")

        market_health = self._market_health(
            strong_buy,
            buy,
            watch,
            total_assets,
        )

        best = ranked[0]

        return {
            "generated_at": datetime.now().strftime("%d-%b-%Y %H:%M:%S"),
            "market_health": market_health,
            "market_status": self._market_status(market_health),
            "total_assets": total_assets,
            "strong_buy": strong_buy,
            "buy": buy,
            "watch": watch,
            "hold": hold,
            "avoid": avoid,
            "top_opportunity": best,
            "top_five": ranked[:5],
            "ranked": ranked,
        }

    # -----------------------------------------------------

    def _market_health(
        self,
        strong_buy,
        buy,
        watch,
        total_assets,
    ):

        if total_assets == 0:
            return 0

        score = (strong_buy * 100 + buy * 80 + watch * 60) / total_assets

        return round(score)

    # -----------------------------------------------------

    def _market_status(self, score):

        if score >= 80:
            return "Very Strong"

        if score >= 65:
            return "Constructive"

        if score >= 50:
            return "Neutral"

        if score >= 35:
            return "Weak"

        return "Defensive"

    # -----------------------------------------------------

    def _empty(self):

        return {
            "generated_at": "",
            "market_health": 0,
            "market_status": "Unavailable",
            "total_assets": 0,
            "strong_buy": 0,
            "buy": 0,
            "watch": 0,
            "hold": 0,
            "avoid": 0,
            "top_opportunity": None,
            "top_five": [],
            "ranked": [],
        }
