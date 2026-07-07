"""
RT-DOS Founder Alpha
Technical Analysis Engine
Version : 0.2.0
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
            ema200 = calculate_ema(history, 200)

            price = item["last_price"]

            if price > ema20 > ema50 > ema200:
                trend = "STRONG BULLISH"

            elif price > ema20 > ema50:
                trend = "BULLISH"

            elif price < ema20 < ema50 < ema200:
                trend = "STRONG BEARISH"

            elif price < ema20 < ema50:
                trend = "BEARISH"

            else:
                trend = "SIDEWAYS"

            results.append(
                {
                    "symbol": item["symbol"],
                    "ltp": price,
                    "ema20": ema20,
                    "ema50": ema50,
                    "ema200": ema200,
                    "trend": trend,
                }
            )

        return results
