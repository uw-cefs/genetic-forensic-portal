from __future__ import annotations

import streamlit as st

import genetic_forensic_portal.app.utils.familial_analysis_utils as fam_utils
from genetic_forensic_portal.app.client import gf_api_client as client

st.header("Get Familial Analysis")

uuid = st.session_state.uuid if "uuid" in st.session_state else None

analysis_list = client.list_analyses()

uuid = st.selectbox(
    "Select a sample ID",
    analysis_list,
    index=st.session_state.index if "index" in st.session_state else None,
    placeholder="Select sample ID...",
)

if uuid:
    try:
        analysis = client.get_familial_analysis(uuid)
        st.dataframe(
            analysis.style.map(
                fam_utils.highlight_exact_matches, subset=fam_utils.EXACT_MATCH_COLUMN
            )
        )
    except FileNotFoundError:
        st.error("Analysis not found")
    except Exception as e:
        st.error(e)
