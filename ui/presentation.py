"""
RT-DOS Intelligence Platform
Module      : Presentation Engine
Version     : 4.0.0
Status      : Production Ready
Architecture: Workspace Framework
"""

from datetime import datetime


class PresentationEngine:
    """
    Converts Decision Engine output into presentation-ready data
    for the RT-DOS Workspace while preserving the existing contract.
    """

    def build(self, decisions):

        normalized = self._normalize_decisions(decisions)

        if not normalized:
            return self._empty()

        ranked = sorted(
            normalized,
            key=lambda item: self._score(item),
            reverse=True,
        )

        total_assets = len(ranked)

        strong_buy = sum(1 for item in ranked if self._decision(item) == "STRONG BUY")
        buy = sum(1 for item in ranked if self._decision(item) == "BUY")
        watch = sum(1 for item in ranked if self._decision(item) == "WATCH")
        hold = sum(1 for item in ranked if self._decision(item) == "HOLD")
        avoid = sum(1 for item in ranked if self._decision(item) == "AVOID")

        market_health = self._market_health(
            strong_buy,
            buy,
            watch,
            total_assets,
        )

        market_status = self._market_status(market_health)
        best = ranked[0] if ranked else None

        return {
            "generated_at": datetime.now().strftime("%d-%b-%Y %H:%M:%S"),
            "market_health": market_health,
            "market_status": market_status,
            "total_assets": total_assets,
            "strong_buy": strong_buy,
            "buy": buy,
            "watch": watch,
            "hold": hold,
            "avoid": avoid,
            "top_opportunity": best,
            "top_five": ranked[:5],
            "ranked": ranked,
            "executive": self._build_executive(
                best,
                market_health,
                market_status,
                strong_buy,
                buy,
                watch,
                hold,
                avoid,
            ),
        }

    # -----------------------------------------------------

    def _normalize_decisions(self, decisions):

        if decisions is None:
            return []

        if isinstance(decisions, (list, tuple)):
            return list(decisions)

        return [decisions]

    # -----------------------------------------------------

    def _score(self, item):

        if isinstance(item, dict):
            return item.get("score", 0)

        return 0

    # -----------------------------------------------------

    def _decision(self, item):

        if isinstance(item, dict):
            return item.get("decision", "HOLD")

        return "HOLD"

    # -----------------------------------------------------

    def _confidence(self, item):

        if not isinstance(item, dict):
            return 0

        confidence = item.get("confidence", 0)

        if isinstance(confidence, str):
            try:
                return int(confidence.rstrip("%"))
            except ValueError:
                return 0

        return int(confidence)

    # -----------------------------------------------------

    def _risk(self, item):

        if not isinstance(item, dict):
            return "MEDIUM"

        return item.get("risk", "MEDIUM")

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

    def _market_bias(self, health):

        if health >= 80:
            return "Bullish"

        if health >= 65:
            return "Constructive"

        if health >= 50:
            return "Neutral"

        if health >= 35:
            return "Cautious"

        return "Defensive"

    # -----------------------------------------------------

    def _market_regime(self, health):

        if health >= 80:
            return "Expansion"

        if health >= 65:
            return "Trend"

        if health >= 50:
            return "Range"

        if health >= 35:
            return "Compression"

        return "Distribution"

    # -----------------------------------------------------

    def _institutional_confidence(self, health, confidence):

        return max(20, min(99, round((health * 0.7) + (confidence * 0.3))))

    # -----------------------------------------------------

    def _expected_move(self, health, confidence):

        if health >= 80 and confidence >= 75:
            return "+3% to +6%"

        if health >= 65:
            return "+1% to +3%"

        if health >= 50:
            return "Flat to +2%"

        if health >= 35:
            return "-1% to +1%"

        return "-2% to -1%"

    # -----------------------------------------------------

    def _holding_period(self, health, decision):

        if decision in {"STRONG BUY", "BUY"} and health >= 65:
            return "1-3 days"

        if decision in {"STRONG BUY", "BUY"}:
            return "3-7 days"

        if health >= 50:
            return "1-2 weeks"

        return "Capital preservation"

    # -----------------------------------------------------

    def _risk_level(self, risk, health):

        risk_text = str(risk).upper()

        if risk_text in {"LOW", "LOW RISK"}:
            return "Low"

        if risk_text in {"MEDIUM", "MODERATE", "MEDIUM RISK"}:
            return "Medium" if health >= 50 else "Elevated"

        return "High"

    # -----------------------------------------------------

    def _trading_plan(self, decision, market_status, risk_level):

        if decision == "STRONG BUY":
            return (
                f"Prioritize disciplined long entries in {market_status.lower()} conditions "
                f"while maintaining strict position sizing and {risk_level.lower()} risk controls."
            )

        if decision == "BUY":
            return (
                f"Look for confirmation setups in {market_status.lower()} conditions and size "
                f"positions conservatively with {risk_level.lower()} risk oversight."
            )

        if decision == "WATCH":
            return "Remain patient, monitor price action, and wait for a higher-conviction trigger before committing capital."

        if decision == "HOLD":
            return "Reduce new exposure and preserve capital until the market structure improves."

        return "Maintain a defensive posture and prioritize capital preservation."

    # -----------------------------------------------------

    def _executive_comment(
        self, best, market_status, market_bias, market_regime, health
    ):

        if best is None:
            return "No actionable intelligence is available at the moment. Monitor the market closely and wait for a clearer setup."

        symbol = (
            best.get("symbol", "the market") if isinstance(best, dict) else "the market"
        )
        decision = best.get("decision", "HOLD") if isinstance(best, dict) else "HOLD"
        confidence = self._confidence(best)

        return (
            f"RT-DOS identifies {symbol} as the leading opportunity with a {decision.lower()} signal. "
            f"The market is currently {market_status.lower()} with {market_bias.lower()} bias and {market_regime.lower()} regime conditions. "
            f"The current confidence level is {confidence}% and the overall health score is {health}%."
        )

    # -----------------------------------------------------

    def _risk_watch(self, health, decision):

        if decision == "STRONG BUY":
            return [
                "Price confirmation at key resistance",
                "Volatility expansion around earnings or macro catalysts",
                "Position sizing discipline",
            ]

        if decision == "BUY":
            return [
                "Breakdown of recent support",
                "Rapid volatility expansion",
                "Weakening trend structure",
            ]

        if health >= 50:
            return [
                "Momentum divergence",
                "Unexpected volatility spikes",
                "Sector rotation into defensive names",
            ]

        return [
            "Extended downside pressure",
            "Liquidity stress",
            "Broad market deterioration",
        ]

    # -----------------------------------------------------

    def _build_executive(
        self,
        best,
        market_health,
        market_status,
        strong_buy,
        buy,
        watch,
        hold,
        avoid,
    ):

        if best is None:
            return {
                "market_bias": "Neutral",
                "market_regime": "Range",
                "institutional_confidence": 50,
                "probability": 50,
                "expected_move": "Flat to +1%",
                "holding_period": "Watchlist",
                "risk_level": "Medium",
                "trading_plan": "Wait for higher-quality confirmation before establishing risk.",
                "executive_comment": "No actionable intelligence is available at the moment.",
                "risk_watch": [
                    "Insufficient signal quality",
                    "Market volatility",
                    "Macro uncertainty",
                ],
            }

        decision = self._decision(best)
        confidence = self._confidence(best)
        risk = self._risk(best)

        return {
            "market_bias": self._market_bias(market_health),
            "market_regime": self._market_regime(market_health),
            "institutional_confidence": self._institutional_confidence(
                market_health, confidence
            ),
            "probability": max(0, min(100, round((confidence + market_health) / 2))),
            "expected_move": self._expected_move(market_health, confidence),
            "holding_period": self._holding_period(market_health, decision),
            "risk_level": self._risk_level(risk, market_health),
            "trading_plan": self._trading_plan(
                decision, market_status, self._risk_level(risk, market_health)
            ),
            "executive_comment": self._executive_comment(
                best,
                market_status,
                self._market_bias(market_health),
                self._market_regime(market_health),
                market_health,
            ),
            "risk_watch": self._risk_watch(market_health, decision),
        }

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
            "executive": {
                "market_bias": "Neutral",
                "market_regime": "Range",
                "institutional_confidence": 50,
                "probability": 50,
                "expected_move": "Flat to +1%",
                "holding_period": "Watchlist",
                "risk_level": "Medium",
                "trading_plan": "Wait for higher-quality confirmation before establishing risk.",
                "executive_comment": "No actionable intelligence is available at the moment.",
                "risk_watch": [
                    "Insufficient signal quality",
                    "Market volatility",
                    "Macro uncertainty",
                ],
            },
        }
