"""
RT-DOS Founder Alpha
Scoring Engine
Version : 0.1.0
"""


class ScoringEngine:

    def calculate(self, analysis):

        results = []

        for item in analysis:

            score = 0

            if item["ltp"] > item["ema20"]:
                score += 2

            if item["ema20"] > item["ema50"]:
                score += 2

            if item["ema50"] > item["ema200"]:
                score += 3

            if item["ltp"] > item["ema200"]:
                score += 3

            results.append(
                {
                    "symbol": item["symbol"],
                    "ltp": item["ltp"],
                    "ema20": item["ema20"],
                    "ema50": item["ema50"],
                    "ema200": item["ema200"],
                    "trend": item["trend"],
                    "score": score,
                }
            )

        return results
