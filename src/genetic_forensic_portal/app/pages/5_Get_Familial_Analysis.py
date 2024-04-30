from __future__ import annotations

import streamlit as st

from genetic_forensic_portal.app.client import gf_api_client as client

st.header("Get Familial Analysis")

uuid = st.selectbox(
    "Select a sample ID",
    client.list_completed_analyses(),
    index=None,
    placeholder="Select sample ID...",
)

if uuid:
    try:
        analysis = client.get_familial_analysis(uuid)
        st.dataframe(analysis)
    except FileNotFoundError:
        st.error("Analysis not found")
