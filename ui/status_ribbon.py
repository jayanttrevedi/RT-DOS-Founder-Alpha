"""
RT-DOS Intelligence Platform
Module      : Executive Status Ribbon
Version     : 1.0.0
Status      : Production
Architecture: Market Command Centre V2
"""

from datetime import datetime, time

import streamlit as st


class StatusRibbon:

    VERSION = "Founder Alpha v4.1"

    # ==========================================================
    # Public
    # ==========================================================

    def show(self):

        session = self._market_session()

        session_icon = {
            "PRE-OPEN": "🟡",
            "OPEN": "🟢",
            "CLOSED": "🔴",
        }.get(session, "⚪")

        now = datetime.now()

        col1, col2, col3, col4, col5, col6 = st.columns(6)

        with col1:
            st.metric(
                "Market",
                f"{session_icon} {session}",
            )

        with col2:
            st.metric(
                "Data",
                "ONLINE",
            )

        with col3:
            st.metric(
                "Validation",
                "ACTIVE",
            )

        with col4:
            st.metric(
                "Consistency",
                "ACTIVE",
            )

        with col5:
            st.metric(
                "Updated",
                now.strftime("%H:%M:%S"),
            )

        with col6:
            st.metric(
                "Version",
                self.VERSION,
            )

        st.divider()

    # ==========================================================
    # Private
    # ==========================================================

    def _market_session(self):

        current = datetime.now().time()

        if time(9, 0) <= current < time(9, 15):
            return "PRE-OPEN"

        if time(9, 15) <= current <= time(15, 30):
            return "OPEN"

        return "CLOSED"
