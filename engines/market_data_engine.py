"""
RT-DOS Founder Alpha
Market Data Engine
Version : 0.1.0
"""


class MarketDataEngine:

    def __init__(self):
        self.engine_name = "Market Data Engine"

    def load(self):

        return {
            "status": True,
            "engine": self.engine_name,
            "message": "Engine Loaded Successfully",
        }
