"""
RT-DOS Founder Alpha
EMA Indicator
Version : 0.1.0
"""


def calculate_ema(history, period):

    closes = history["Close"]

    ema = closes.ewm(span=period, adjust=False).mean()

    return float(ema.iloc[-1])
