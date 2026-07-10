"""
RT-DOS Intelligence Platform
Module      : Executive Alerts UI
Version     : 1.0.0
Status      : Production Ready
Architecture: RT-DOS Presentation Layer
"""

from __future__ import annotations

from typing import Any, Dict, List

import streamlit as st


class ExecutiveAlerts:
    """Render Market Sentinel alerts as a presentation-only UI component.

    This component is intentionally passive. It receives a sentinel payload from
    the engine and displays the alert data without performing calculations or
    business-rule evaluation.
    """

    def show(self, sentinel: Dict[str, Any]) -> None:
        """Render sentinel alerts grouped by severity.

        Args:
            sentinel: A dictionary-like payload returned by the MarketSentinelEngine.
        """

        st.subheader("Executive Alerts")

        if not isinstance(sentinel, dict):
            st.warning("No sentinel data available.")
            return

        alerts = sentinel.get("alerts") or []

        if not isinstance(alerts, list):
            alerts = []

        self._render_section(
            title="🔴 Critical Alerts",
            severity="CRITICAL",
            alerts=alerts,
            empty_message="No critical alerts.",
            container_fn=st.success,
        )

        self._render_section(
            title="🟠 High Priority Alerts",
            severity="HIGH",
            alerts=alerts,
            empty_message="No high priority alerts.",
            container_fn=st.info,
        )

        self._render_section(
            title="🟢 Information",
            severity="INFO",
            alerts=alerts,
            empty_message="No informational alerts.",
            container_fn=st.caption,
        )

    def _render_section(
        self,
        title: str,
        severity: str,
        alerts: List[Dict[str, Any]],
        empty_message: str,
        container_fn: Any,
    ) -> None:
        """Render a single alert section for the requested severity.

        Args:
            title: The display title for the section.
            severity: The severity value to filter for.
            alerts: The alert list to render.
            empty_message: The message shown when no alerts are present.
            container_fn: Streamlit render function for empty state styling.
        """

        st.markdown(f"### {title}")

        matching_alerts = [
            alert for alert in alerts if alert.get("severity") == severity
        ]

        if not matching_alerts:
            container_fn(empty_message)
            return

        for alert in matching_alerts:
            with st.container():
                title_text = alert.get("title") or "Untitled Alert"
                message = alert.get("message") or ""
                timestamp = alert.get("timestamp") or ""

                st.write(f"**{title_text}**")
                st.write(message)
                st.caption(timestamp)
                st.divider()
