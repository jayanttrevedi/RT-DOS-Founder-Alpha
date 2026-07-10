"""
RT-DOS Intelligence Platform
Module      : Application Controller
Version     : 5.0.0
Status      : Production
Architecture: Workspace Framework
"""

import streamlit as st

from engines.market_data_engine import MarketDataEngine
from engines.validation_engine import ValidationEngine
from engines.intelligence_pipeline import IntelligencePipeline
from engines.decision_engine import DecisionEngine

from ui.theme import apply_theme
from ui.navigation import Navigation
from ui.presentation import PresentationEngine
from ui.workspace_router import WorkspaceRouter

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
# Navigation
# ==========================================================

selected_workspace = Navigation().show()

# ==========================================================
# Intelligence Pipeline
# ==========================================================

with st.spinner("Loading RT-DOS Intelligence Platform..."):

    # ------------------------------------------------------
    # Market Data
    # ------------------------------------------------------

    market_engine = MarketDataEngine()

    result = market_engine.load()

    if not result["status"]:

        st.error("Market Data Engine Failed")
        st.stop()

    # ------------------------------------------------------
    # Validation
    # ------------------------------------------------------

    validation = ValidationEngine().validate(result["market_data"])

    if not validation["report"]["success"]:

        st.error("Market Data Validation Failed")
        st.json(validation["report"])
        st.stop()

    market_data = validation["valid_assets"]

    # ------------------------------------------------------
    # Intelligence Pipeline
    # ------------------------------------------------------

    try:

        intelligence = IntelligencePipeline().run(market_data)

    except Exception as e:

        st.error("Intelligence Pipeline Failed")

        st.exception(e)

        st.stop()

    # ------------------------------------------------------
    # Decision Engine
    # ------------------------------------------------------

    decisions = DecisionEngine().analyze(intelligence)

# ==========================================================
# Presentation
# ==========================================================

presentation = PresentationEngine().build(decisions)

# ==========================================================
# Workspace
# ==========================================================

WorkspaceRouter().show(
    selected_workspace,
    presentation,
)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption("RT-DOS Founder Alpha v5.0 | Workspace Framework")
