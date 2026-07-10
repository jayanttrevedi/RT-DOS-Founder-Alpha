"""
RT-DOS Intelligence Platform
Module      : Application Controller
Version     : 4.0.0
Status      : Production
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
from engines.validation_engine import ValidationEngine
from engines.consistency_engine import ConsistencyEngine

from ui.theme import apply_theme
from ui.presentation import PresentationEngine
from ui.navigation import Navigation
from ui.workspace_router import WorkspaceRouter

# ==========================================================
# Streamlit
# ==========================================================

st.set_page_config(
    page_title="RT-DOS Intelligence Platform",
    page_icon="📈",
    layout="wide",
)

apply_theme()

# ==========================================================
# Navigation
# ==========================================================

selected_workspace = Navigation().show()

# ==========================================================
# Intelligence Pipeline
# ==========================================================

with st.spinner("Loading RT-DOS Intelligence Platform..."):

    market_engine = MarketDataEngine()

    result = market_engine.load()

    if not result["status"]:

        st.error("Market Data Engine Failed")
        st.stop()

    validation = ValidationEngine().validate(result["market_data"])

    if not validation["report"]["success"]:

        st.error("Market Data Validation Failed")

        st.json(validation["report"])

        st.stop()

    market_data = validation["valid_assets"]

    technical = TechnicalEngine().analyze(market_data)

    scored = ScoringEngine().calculate(technical)

    momentum = MomentumEngine().analyze(market_data)

    atr = ATREngine().analyze(market_data)

    volume = VolumeEngine().analyze(market_data)

    relative_strength = RelativeStrengthEngine().analyze(market_data)

    consistency = ConsistencyEngine().validate(
        technical,
        momentum,
        atr,
        volume,
        relative_strength,
    )

    if not consistency["success"]:

        st.error("Engine Consistency Validation Failed")

        st.json(consistency)

        st.stop()

    composite = CompositeEngine().calculate(
        scored,
        momentum,
        atr,
        volume,
        relative_strength,
    )

    decisions = DecisionEngine().analyze(composite)

# ==========================================================
# Presentation
# ==========================================================

presentation = PresentationEngine().build(decisions)

# ==========================================================
# Workspace Router
# ==========================================================

WorkspaceRouter().show(
    selected_workspace,
    presentation,
)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption("RT-DOS Founder Alpha v4.0 | Workspace Framework")
