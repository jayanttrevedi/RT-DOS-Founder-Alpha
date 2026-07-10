"""
RT-DOS Intelligence Platform
Module      : Workspace Router
Version     : 1.0.0
Status      : Production
Architecture: Workspace Framework

Purpose
-------
Routes the selected workspace to the appropriate UI.

This is the central navigation hub for all RT-DOS workspaces.
"""

import streamlit as st

from ui.dashboard import Dashboard


class WorkspaceRouter:

    def __init__(self):

        self.routes = {
            "Market Command Centre": self._market_command_centre,
            "Opportunity Scanner": self._coming_soon,
            "Watchlist Intelligence": self._coming_soon,
            "Portfolio Intelligence": self._coming_soon,
            "Options Intelligence": self._coming_soon,
            "Sector Rotation": self._coming_soon,
            "Market Breadth": self._coming_soon,
            "AI Intelligence": self._coming_soon,
            "Explainability": self._coming_soon,
            "Settings": self._coming_soon,
        }

    # =====================================================

    def show(self, workspace, presentation):

        page = self.routes.get(
            workspace,
            self._coming_soon,
        )

        page(presentation)

    # =====================================================

    def _market_command_centre(self, presentation):

        Dashboard().show(presentation)

    # =====================================================

    def _coming_soon(self, presentation):

        st.title("🚧 Workspace Under Development")

        st.info("This workspace will become available in the next development phases.")

        st.write("Current Workspace:")

        st.code(
            st.session_state.get(
                "workspace",
                "Unknown",
            )
        )
