from __future__ import annotations

import streamlit as st

from genetic_forensic_portal.app.client import gf_api_client as client


def try_get_analysis(uuid: str) -> str:
    try:
        return client.get_analysis_status(uuid)
    except FileNotFoundError:
        return "NOT FOUND"
    except Exception:
        return "ERROR"


def update_session_state(uuid: str, index: int) -> None:
    st.session_state.uuid = uuid
    st.session_state.index = index


st.header("List Analyses")

analyses = client.list_analyses()

# TODO see if i can reorder rows so completed analyses are at the top
# TODO color highlight based on status
# TODO title columns
# TODO pagination????
for index, analysis in enumerate(analyses):
    ana_col, status_col, scat_col, vor_col, fam_col = st.columns([1, 1, 0.5, 0.5, 0.5])
    ana_col.write(analysis)
    status_col.write(try_get_analysis(analysis))
    with scat_col:
        if st.button(key=f"SCAT {analysis}", label="SCAT"):
            update_session_state(analysis, index)
            st.switch_page("pages/4_Get_SCAT_Analysis.py")
    with vor_col:
        if st.button(key=f"Voronoi {analysis}", label="Voronoi"):
            update_session_state(analysis, index)
            st.switch_page("pages/5_Get_Voronoi_Analysis.py")
    with fam_col:
        if st.button(key=f"Familial {analysis}", label="Familial"):
            update_session_state(analysis, index)
            st.switch_page("pages/6_Get_Familial_Analysis.py")
