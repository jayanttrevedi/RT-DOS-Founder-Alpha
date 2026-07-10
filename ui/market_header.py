"""
RT-DOS Intelligence Platform
Module      : Market Command Centre Header
Version     : 2.0.0
Status      : Production
Architecture: Market Command Centre V2
"""

from datetime import datetime

import streamlit as st

from ui.status_ribbon import StatusRibbon


class MarketHeader:

    VERSION = "Founder Alpha v4.1"

    # ==========================================================

    def show(self):

        # ------------------------------------------------------
        # Executive Status Ribbon
        # ------------------------------------------------------

        StatusRibbon().show()

        # ------------------------------------------------------
        # Main Header
        # ------------------------------------------------------

        left, right = st.columns([4, 1])

        with left:

            st.title("📈 RT-DOS Market Command Centre")

            st.caption("Retail Trading Decision Operating System")

        with right:

            st.metric(
                "Date",
                datetime.now().strftime("%d-%b-%Y"),
            )

        st.caption(f"RT-DOS {self.VERSION} | Workspace : Market Command Centre")

        st.divider()
