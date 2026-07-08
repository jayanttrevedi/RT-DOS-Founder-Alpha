"""
RT-DOS Founder Alpha
Composite Intelligence Engine
Version : 1.4.0
"""


class CompositeEngine:

    def calculate(self, technical, momentum, atr, volume, relative_strength):

        results = []

        momentum_map = {item["symbol"]: item for item in momentum}

        atr_map = {item["symbol"]: item for item in atr}

        volume_map = {item["symbol"]: item for item in volume}

        rs_map = {item["symbol"]: item for item in relative_strength}

        for item in technical:

            symbol = item["symbol"]

            trend_score = item["score"] * 3

            m = momentum_map[symbol]
            a = atr_map[symbol]
            v = volume_map[symbol]
            r = rs_map[symbol]

            # ------------------------
            # Momentum Score (20)
            # ------------------------

            if m["momentum"] == "STRONG":
                momentum_score = 20

            elif m["momentum"] == "NEUTRAL":
                momentum_score = 12

            elif m["momentum"] == "WEAK":
                momentum_score = 6

            elif m["momentum"] == "OVERBOUGHT":
                momentum_score = 10

            else:
                momentum_score = 8

            # ------------------------
            # ATR Score (15)
            # ------------------------

            if a["volatility"] == "VERY HIGH":
                volatility_score = 15

            elif a["volatility"] == "HIGH":
                volatility_score = 12

            elif a["volatility"] == "MEDIUM":
                volatility_score = 8

            else:
                volatility_score = 3

            # ------------------------
            # Volume Score (15)
            # ------------------------

            if v["volume_strength"] == "EXPLOSIVE":
                volume_score = 15

            elif v["volume_strength"] == "HIGH":
                volume_score = 12

            elif v["volume_strength"] == "NORMAL":
                volume_score = 8

            else:
                volume_score = 3

            # ------------------------
            # Relative Strength (20)
            # ------------------------

            if r["strength"] == "LEADER":
                rs_score = 20

            elif r["strength"] == "STRONG":
                rs_score = 16

            elif r["strength"] == "NEUTRAL":
                rs_score = 10

            else:
                rs_score = 4

            total_score = (
                trend_score
                + momentum_score
                + volatility_score
                + volume_score
                + rs_score
            )

            if total_score >= 85:
                grade = "A+"

            elif total_score >= 75:
                grade = "A"

            elif total_score >= 65:
                grade = "B+"

            elif total_score >= 55:
                grade = "B"

            else:
                grade = "C"

            results.append(
                {
                    "symbol": symbol,
                    "score": total_score,
                    "grade": grade,
                    "trend": trend_score,
                    "momentum": momentum_score,
                    "volatility": volatility_score,
                    "volume": volume_score,
                    "relative_strength": rs_score,
                }
            )

        return results
