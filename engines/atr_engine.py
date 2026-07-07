"""
RT-DOS Founder Alpha
ATR Engine
Version : 1.1.0
"""

from indicators.atr import calculate_atr


class ATREngine:

    def analyze(self, market_data):

        results = []

        for item in market_data:

            history = item["history"]

            if history is None:
                continue

            atr = calculate_atr(history)

            if atr >= 500:
                volatility = "VERY HIGH"

            elif atr >= 200:
                volatility = "HIGH"

            elif atr >= 50:
                volatility = "MEDIUM"

            else:
                volatility = "LOW"

            results.append(
                {"symbol": item["symbol"], "atr": atr, "volatility": volatility}
            )

        return results
