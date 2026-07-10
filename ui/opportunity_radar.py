"""
RT-DOS Intelligence Platform
Module      : Opportunity Radar
Version     : 1.0.0
Status      : Production
Architecture: Workspace Framework
"""

import streamlit as st


class OpportunityRadar:

    def show(self, presentation):

        st.subheader("🎯 Opportunity Radar")

        opportunities = presentation.get("top_five", [])

        if not opportunities:

            st.info("No trading opportunities available.")
            return

        for rank, asset in enumerate(opportunities, start=1):

            with st.container():

                left, right = st.columns([5, 2])

                with left:

                    st.markdown(f"### {rank}. {asset['symbol']}")

                    st.write(
                        f"**Decision:** {asset['decision']}  |  "
                        f"**Grade:** {asset['grade']}"
                    )

                with right:

                    st.metric(
                        "Score",
                        asset["score"],
                    )

                    st.metric(
                        "Confidence",
                        f"{asset['confidence']}%",
                    )

                    st.metric(
                        "Risk",
                        asset["risk"],
                    )

                st.divider()
