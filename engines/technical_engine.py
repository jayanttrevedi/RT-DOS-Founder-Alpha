"""
RT-DOS Founder Alpha
Technical Analysis Engine
Version : 0.1.0
"""

from indicators.ema import calculate_ema


class TechnicalEngine:

    def analyze(self, market_data):

        results = []

        for item in market_data:

            history = item["history"]

            if history is None:

                continue

            ema20 = calculate_ema(history, 20)
            ema50 = calculate_ema(history, 50)

            results.append(
                {
                    "symbol": item["symbol"],
                    "ltp": item["last_price"],
                    "ema20": ema20,
                    "ema50": ema50,
                }
            )

        return results
