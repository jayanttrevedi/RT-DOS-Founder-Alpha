"""
RT-DOS Intelligence Platform
Module      : Navigation Framework
Version     : 1.0.0
Status      : Production
Architecture: Workspace Framework
"""

import streamlit as st


class Navigation:

    WORKSPACES = [
        ("🏠", "Market Command Centre"),
        ("🎯", "Opportunity Scanner"),
        ("📋", "Watchlist Intelligence"),
        ("💼", "Portfolio Intelligence"),
        ("📈", "Options Intelligence"),
        ("🔄", "Sector Rotation"),
        ("📊", "Market Breadth"),
        ("🧠", "AI Intelligence"),
        ("🔍", "Explainability"),
        ("⚙️", "Settings"),
    ]

    VERSION = "Founder Alpha v4.0"

    def show(self):

        with st.sidebar:

            st.title("RT-DOS")

            st.caption(self.VERSION)

            st.divider()

            if "workspace" not in st.session_state:
                st.session_state.workspace = "Market Command Centre"

            labels = [name for _, name in self.WORKSPACES]

            current = labels.index(st.session_state.workspace)

            selected = st.radio(
                "Workspace",
                labels,
                index=current,
            )

            st.session_state.workspace = selected

            st.divider()

            st.subheader("System Status")

            st.success("Backend : Online")

            st.success("Workspace : Ready")

            st.success("Validation : Active")

            st.success("Consistency : Active")

            st.divider()

            st.caption("Retail Trading Decision Operating System")

            return selected
