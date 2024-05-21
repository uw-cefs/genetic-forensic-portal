from __future__ import annotations

import streamlit as st

from genetic_forensic_portal.app.client import gf_api_client as client
from genetic_forensic_portal.utils.analysis_status import AnalysisStatus


def try_get_analysis(uuid: str) -> AnalysisStatus:
    try:
        return client.get_analysis_status(uuid)
    except FileNotFoundError:
        return AnalysisStatus.ANALYSIS_NOT_FOUND
    except Exception:
        return AnalysisStatus.ANALYSIS_ERROR


def update_session_state(uuid: str, index: int) -> None:
    st.session_state.uuid = uuid
    st.session_state.index = index


st.header("List Analyses")

analyses = client.list_analyses()
statuses = [try_get_analysis(analysis) for analysis in analyses]

results = zip(range(len(analyses)), analyses, statuses)
results = sorted(results, key=lambda x: x[2])

statuses = [try_get_analysis(analysis) for analysis in analyses]

results = zip(range(len(analyses)), analyses, statuses, strict=True)
sorted_results = sorted(results, key=lambda x: x[2])

ana_col, status_col, scat_col, vor_col, fam_col = st.columns([1, 0.7, 0.5, 0.5, 0.5])
ana_col.write("**Analysis ID**")
status_col.write("**Status**")
scat_col.write("**SCAT Analysis**")
vor_col.write("**Voronoi Analysis**")
fam_col.write("**Familial Analysis**")

for index, analysis, status in sorted_results:
    ana_col, status_col, scat_col, vor_col, fam_col = st.columns(
        [1, 0.7, 0.5, 0.5, 0.5]
    )
    ana_col.write(analysis)
    status_col.write(status.value)
    with scat_col:
        if st.button(key=f"SCAT {analysis}", label="SCAT", use_container_width=True):
            update_session_state(analysis, index)
            st.switch_page("pages/4_Get_SCAT_Analysis.py")
    with vor_col:
        if st.button(
            key=f"Voronoi {analysis}", label="Voronoi", use_container_width=True
        ):
            update_session_state(analysis, index)
            st.switch_page("pages/5_Get_Voronoi_Analysis.py")
    with fam_col:
        if st.button(
            key=f"Familial {analysis}", label="Familial", use_container_width=True
        ):
            update_session_state(analysis, index)
            st.switch_page("pages/6_Get_Familial_Analysis.py")
