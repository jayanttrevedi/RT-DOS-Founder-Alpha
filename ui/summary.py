"""
RT-DOS Intelligence Platform
Module      : Executive Intelligence Card
Version     : 3.0.0
Status      : Production Candidate
Architecture: Workspace Framework
"""

import streamlit as st


class SummaryPanel:

    def show(self, presentation):

        top = presentation.get("top_opportunity")

        if top is None:

            st.info("No market intelligence available.")

            return

        st.subheader("🧠 Executive Intelligence")

        left, right = st.columns(2)

        # ----------------------------------------
        # Left Column
        # ----------------------------------------

        with left:

            st.metric(
                "Top Opportunity",
                top["symbol"],
            )

            st.metric(
                "Decision",
                top["decision"],
            )

            st.metric(
                "Confidence",
                f'{top["confidence"]}%',
            )

        # ----------------------------------------
        # Right Column
        # ----------------------------------------

        with right:

            st.metric(
                "Composite Score",
                top["score"],
            )

            st.metric(
                "Grade",
                top["grade"],
            )

            st.metric(
                "Risk",
                top["risk"],
            )

        st.success(f"""
### Executive Summary

**Assets Analysed :** {presentation['total_assets']}

**Market Status :** {presentation['market_status']}

**Market Health :** {presentation['market_health']}%

**Top Opportunity :** {top['symbol']}

**Recommended Action :** {top['decision']}

**Confidence :** {top['confidence']}%
""")
