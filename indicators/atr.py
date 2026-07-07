"""
RT-DOS Founder Alpha
ATR Indicator
Version : 1.1.0
"""


def calculate_atr(history, period=14):

    high = history["High"]
    low = history["Low"]
    close = history["Close"]

    previous_close = close.shift(1)

    tr1 = high - low
    tr2 = (high - previous_close).abs()
    tr3 = (low - previous_close).abs()

    true_range = tr1.combine(tr2, max).combine(tr3, max)

    atr = true_range.rolling(period).mean()

    return float(atr.iloc[-1])
