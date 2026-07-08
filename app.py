import streamlit as st
import pandas as pd

from engines.market_data_engine import MarketDataEngine
from engines.technical_engine import TechnicalEngine
from engines.scoring_engine import ScoringEngine
from engines.momentum_engine import MomentumEngine
from engines.atr_engine import ATREngine
from engines.volume_engine import VolumeEngine
from engines.relative_strength_engine import RelativeStrengthEngine
from engines.composite_engine import CompositeEngine
from engines.decision_engine import DecisionEngine
from ui.market_health import show_market_health

st.set_page_config(
    page_title="RT-DOS Intelligence Platform",
    page_icon="📈",
    layout="wide",
)

st.title("📈 RT-DOS Intelligence Platform")
st.subheader("Founder Alpha Prototype")
st.caption("Intelligence Before Execution")

st.divider()
market_health = round(
    (buy * 100 + watch * 60 + strong_buy * 100) / max(len(decisions), 1)
)

left, right = st.columns([1, 2])

with left:
    show_market_health(market_health)

with right:
    st.subheader("📢 Executive Market Status")

    if market_health >= 80:
        st.success("Very Strong Market")

    elif market_health >= 60:
        st.info("Constructive Market")

    elif market_health >= 40:
        st.warning("Mixed Market")

    else:
        st.error("Weak Market")

with st.spinner("Loading Market Intelligence..."):

    market_engine = MarketDataEngine()
    result = market_engine.load()

    if not result["status"]:
        st.error("Unable to load market data.")
        st.stop()

    technical = TechnicalEngine().analyze(result["market_data"])
    scored = ScoringEngine().calculate(technical)
    momentum = MomentumEngine().analyze(result["market_data"])
    atr = ATREngine().analyze(result["market_data"])
    volume = VolumeEngine().analyze(result["market_data"])
    rs = RelativeStrengthEngine().analyze(result["market_data"])

    composite = CompositeEngine().calculate(scored, momentum, atr, volume, rs)

    decisions = DecisionEngine().analyze(composite)

# -----------------------------
# KPI Cards
# -----------------------------

watch = sum(1 for d in decisions if d["decision"] == "WATCH")
buy = sum(1 for d in decisions if d["decision"] == "BUY")
strong_buy = sum(1 for d in decisions if d["decision"] == "STRONG BUY")
avoid = sum(1 for d in decisions if d["decision"] == "AVOID")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.info(f"### 📊 Assets\n## {len(decisions)}")

with col2:
    st.warning(f"### 👀 Watch\n## {watch}")

with col3:
    st.success(f"### ✅ Buy\n## {buy}")

with col4:
    st.success(f"### 🚀 Strong Buy\n## {strong_buy}")

with col5:
    st.error(f"### ⛔ Avoid\n## {avoid}")

st.divider()
table = pd.DataFrame(decisions)
table = table.sort_values("score", ascending=False)

# -----------------------------
# Opportunity Table
# -----------------------------

left, right = st.columns([2, 1])

with left:

    st.subheader("🏆 Market Intelligence Ranking")

    st.caption("RT-DOS Composite Intelligence")

    display = table[
        [
            "symbol",
            "score",
            "grade",
            "decision",
            "confidence",
            "risk",
        ]
    ]

    st.dataframe(
        display,
        use_container_width=True,
        hide_index=True,
    )

with right:

    st.subheader("⭐ Top Opportunity")

    best = table.iloc[0]

    st.metric("Asset", best["symbol"])
    st.metric("Score", best["score"])
    st.metric("Decision", best["decision"])
    st.metric("Confidence", f'{best["confidence"]}%')
    st.metric("Risk", best["risk"])
    st.divider()

st.subheader("🧠 Executive Intelligence Summary")

st.success(f"""
The RT-DOS Intelligence Engine analysed **{len(decisions)} assets**.

Highest Ranked Asset : **{best["symbol"]}**

Recommended Action : **{best["decision"]}**

Composite Score : **{best["score"]}**

Confidence : **{best["confidence"]}%**
""")
