"""
RT-DOS Founder Alpha
Explainability Engine
Version : 1.7.0
"""


class ExplainabilityEngine:

    def generate(self, decisions):

        results = []

        for item in decisions:

            reasons = []
            warnings = []

            score = item["score"]

            if score >= 75:
                reasons.append("Strong overall intelligence score")

            elif score >= 60:
                reasons.append("Positive market structure")

            else:
                warnings.append("Weak overall intelligence score")

            if item["decision"] in ["BUY", "STRONG BUY"]:
                reasons.append("Trend and momentum are aligned")
                reasons.append("Risk profile is favourable")

            elif item["decision"] == "WATCH":
                reasons.append("Setup is developing")
                warnings.append("Waiting for stronger confirmation")

            elif item["decision"] == "HOLD":
                warnings.append("Mixed intelligence signals")

            else:
                warnings.append("Avoid until conditions improve")

            results.append(
                {
                    "symbol": item["symbol"],
                    "score": item["score"],
                    "grade": item["grade"],
                    "decision": item["decision"],
                    "confidence": item["confidence"],
                    "risk": item["risk"],
                    "reasons": reasons,
                    "warnings": warnings,
                }
            )

        return results
