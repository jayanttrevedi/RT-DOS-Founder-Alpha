"""
RT-DOS Intelligence Platform
Executive Summary Panel
Version : 2.0.0
"""

import streamlit as st


class SummaryPanel:

    def show(self, presentation):

        top = presentation["top_asset"]

        if top is None:
            st.warning("No market data available.")
            return

        st.subheader("🧠 Executive Intelligence Summary")

        col1, col2 = st.columns([1, 1])

        with col1:

            st.metric("Top Opportunity", top["symbol"])

            st.metric("Decision", top["decision"])

            st.metric("Confidence", f'{top["confidence"]}%')

        with col2:

            st.metric("Composite Score", top["score"])

            st.metric("Grade", top["grade"])

            st.metric("Risk", top["risk"])

        st.success(f"""
RT-DOS analysed **{presentation['total_assets']} assets**.

Highest Ranked Asset : **{top['symbol']}**

Recommended Action : **{top['decision']}**

Confidence Level : **{top['confidence']}%**

Market Health : **{presentation['market_health']}%**
""")
