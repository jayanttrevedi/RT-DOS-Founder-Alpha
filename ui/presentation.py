"""
RT-DOS Intelligence Platform
Presentation Layer
Version : 2.0.0
"""


class PresentationEngine:

    def prepare(self, decisions):

        ranked = sorted(
            decisions,
            key=lambda x: x["score"],
            reverse=True,
        )

        strong_buy = sum(1 for x in ranked if x["decision"] == "STRONG BUY")

        buy = sum(1 for x in ranked if x["decision"] == "BUY")

        watch = sum(1 for x in ranked if x["decision"] == "WATCH")

        hold = sum(1 for x in ranked if x["decision"] == "HOLD")

        avoid = sum(1 for x in ranked if x["decision"] == "AVOID")

        market_health = round(
            (strong_buy * 100 + buy * 85 + watch * 60 + hold * 40) / max(len(ranked), 1)
        )

        return {
            "ranked": ranked,
            "market_health": market_health,
            "strong_buy": strong_buy,
            "buy": buy,
            "watch": watch,
            "hold": hold,
            "avoid": avoid,
            "total_assets": len(ranked),
            "top_asset": ranked[0] if ranked else None,
        }
