"""
RT-DOS Intelligence Platform
Module      : Position Guardian UI
Version     : 1.0.0
Status      : Production Ready
Architecture: RT-DOS Presentation Layer
"""

from __future__ import annotations

from typing import Any, Dict

import streamlit as st


class PositionGuardian:
    """Render Position Guardian output as a presentation-only UI component.

    This component receives a guardian payload from the PositionGuardianEngine
    and renders it without performing calculations or business-rule evaluation.
    """

    def show(self, guardian: Dict[str, Any]) -> None:
        """Render the position guardian recommendations.

        Args:
            guardian: A dictionary-like payload from the PositionGuardianEngine.
        """

        st.subheader("Position Guardian")

        if not isinstance(guardian, dict):
            st.warning("No position guardian data available.")
            return

        st.subheader(guardian.get("recommendation", "HOLD"))

        st.metric("Risk Level", guardian.get("risk_level", "N/A"))
        st.metric("Confidence", guardian.get("confidence", "N/A"))

        st.info(guardian.get("reason", "No reason provided."))
        st.success(guardian.get("recommended_action", "No action provided."))

        st.metric("Stop Loss Action", guardian.get("stop_loss_action", "N/A"))
        st.metric("Position Size Action", guardian.get("position_size_action", "N/A"))

        if guardian.get("emergency_exit") is True:
            st.error("Emergency Exit Recommended")
        else:
            st.success("No Emergency Exit Required")
