"""
RT-DOS Founder Alpha
Momentum Engine
Version : 0.1.0
"""

from indicators.rsi import calculate_rsi


class MomentumEngine:

    def analyze(self, market_data):

        results = []

        for item in market_data:

            history = item["history"]

            if history is None:
                continue

            rsi = calculate_rsi(history)

            if rsi >= 70:
                momentum = "OVERBOUGHT"
                score = 2

            elif rsi >= 60:
                momentum = "STRONG"
                score = 8

            elif rsi >= 40:
                momentum = "NEUTRAL"
                score = 5

            elif rsi >= 30:
                momentum = "WEAK"
                score = 3

            else:
                momentum = "OVERSOLD"
                score = 7

            results.append(
                {
                    "symbol": item["symbol"],
                    "rsi": rsi,
                    "momentum": momentum,
                    "momentum_score": score,
                }
            )

        return results
