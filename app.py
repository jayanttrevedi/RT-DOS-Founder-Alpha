"""
RT-DOS Intelligence Platform
Module      : Workspace Controller
Version     : 3.0.0
Status      : Production Candidate
Architecture: Workspace Framework
"""

import streamlit as st

from engines.market_data_engine import MarketDataEngine
from engines.technical_engine import TechnicalEngine
from engines.scoring_engine import ScoringEngine
from engines.momentum_engine import MomentumEngine
from engines.atr_engine import ATREngine
from engines.volume_engine import VolumeEngine
from engines.relative_strength_engine import RelativeStrengthEngine
from engines.composite_engine import CompositeEngine
from engines.decision_engine import DecisionEngine

from ui.theme import apply_theme
from ui.presentation import PresentationEngine
from ui.dashboard import Dashboard

# ==========================================================
# Streamlit Configuration
# ==========================================================

st.set_page_config(
    page_title="RT-DOS Intelligence Platform",
    page_icon="📈",
    layout="wide",
)

apply_theme()


# ==========================================================
# Intelligence Pipeline
# ==========================================================

with st.spinner("Loading RT-DOS Intelligence Platform..."):

    market_engine = MarketDataEngine()

    result = market_engine.load()

    if not result["status"]:

        st.error("Market Data Engine Failed")

        st.stop()

    technical = TechnicalEngine().analyze(result["market_data"])

    scored = ScoringEngine().calculate(technical)

    momentum = MomentumEngine().analyze(result["market_data"])

    atr = ATREngine().analyze(result["market_data"])

    volume = VolumeEngine().analyze(result["market_data"])

    relative_strength = RelativeStrengthEngine().analyze(result["market_data"])

    composite = CompositeEngine().calculate(
        scored,
        momentum,
        atr,
        volume,
        relative_strength,
    )

    decisions = DecisionEngine().analyze(composite)


# ==========================================================
# Presentation Layer
# ==========================================================

presentation = PresentationEngine().build(decisions)


# ==========================================================
# Workspace
# ==========================================================

Dashboard().show(presentation)


# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption("RT-DOS Platform v3.0 | Retail Trading Decision Operating System")
