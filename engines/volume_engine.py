"""
RT-DOS Founder Alpha
Volume Intelligence Engine
Version : 1.2.0
"""


class VolumeEngine:

    def analyze(self, market_data):

        results = []

        for item in market_data:

            history = item["history"]

            if history is None:
                continue

            current_volume = int(history["Volume"].iloc[-1])

            average_volume = float(history["Volume"].tail(20).mean())

            if average_volume == 0:
                volume_ratio = 0.0
            else:
                volume_ratio = current_volume / average_volume

            if volume_ratio >= 2.0:
                volume_strength = "EXPLOSIVE"

            elif volume_ratio >= 1.5:
                volume_strength = "HIGH"

            elif volume_ratio >= 1.0:
                volume_strength = "NORMAL"

            else:
                volume_strength = "LOW"

            results.append(
                {
                    "symbol": item["symbol"],
                    "current_volume": current_volume,
                    "average_volume": round(average_volume, 2),
                    "volume_ratio": round(volume_ratio, 2),
                    "volume_strength": volume_strength,
                }
            )

        return results
