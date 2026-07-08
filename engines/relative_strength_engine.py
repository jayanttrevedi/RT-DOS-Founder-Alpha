"""
RT-DOS Founder Alpha
Relative Strength Intelligence Engine
Version : 1.4.0
"""


class RelativeStrengthEngine:

    def analyze(self, market_data):

        results = []

        benchmark = None

        for item in market_data:
            if item["symbol"] == "NIFTY":
                benchmark = item
                break

        if benchmark is None:
            return results

        benchmark_history = benchmark.get("history")

        if benchmark_history is None:
            return results

        if len(benchmark_history) < 20:
            return results

        benchmark_return = (
            (benchmark_history["Close"].iloc[-1] - benchmark_history["Close"].iloc[-20])
            / benchmark_history["Close"].iloc[-20]
        ) * 100

        for item in market_data:

            history = item.get("history")

            if history is None:
                continue

            if len(history) < 20:
                continue

            asset_return = (
                (history["Close"].iloc[-1] - history["Close"].iloc[-20])
                / history["Close"].iloc[-20]
            ) * 100

            relative_strength = asset_return - benchmark_return

            if relative_strength >= 5:
                strength = "LEADER"
            elif relative_strength >= 2:
                strength = "STRONG"
            elif relative_strength >= -2:
                strength = "NEUTRAL"
            else:
                strength = "WEAK"

            results.append(
                {
                    "symbol": item["symbol"],
                    "asset_return": round(asset_return, 2),
                    "benchmark_return": round(benchmark_return, 2),
                    "relative_strength": round(relative_strength, 2),
                    "strength": strength,
                }
            )

        return results
