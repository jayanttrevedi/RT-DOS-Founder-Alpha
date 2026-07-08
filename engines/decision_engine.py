"""
RT-DOS Founder Alpha
Decision Intelligence Engine
Version : 1.5.0
"""


class DecisionEngine:

    def analyze(self, composite):

        results = []

        for item in composite:

            score = item["score"]

            if score >= 85:
                decision = "STRONG BUY"
                confidence = 95
                risk = "LOW"

            elif score >= 75:
                decision = "BUY"
                confidence = 85
                risk = "LOW"

            elif score >= 60:
                decision = "WATCH"
                confidence = 70
                risk = "MEDIUM"

            elif score >= 40:
                decision = "HOLD"
                confidence = 50
                risk = "MEDIUM"

            else:
                decision = "AVOID"
                confidence = 30
                risk = "HIGH"

            results.append(
                {
                    "symbol": item["symbol"],
                    "score": score,
                    "grade": item["grade"],
                    "decision": decision,
                    "confidence": confidence,
                    "risk": risk,
                }
            )

        return results
