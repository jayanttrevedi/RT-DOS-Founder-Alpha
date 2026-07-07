"""
RT-DOS Founder Alpha
RSI Indicator
Version : 0.1.0
"""


def calculate_rsi(history, period=14):

    close = history["Close"]

    delta = close.diff()

    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    average_gain = gain.rolling(period).mean()
    average_loss = loss.rolling(period).mean()

    rs = average_gain / average_loss

    rsi = 100 - (100 / (1 + rs))

    return float(rsi.iloc[-1])
