# src/genetic_forensic_portal/util/status_enum.py
from __future__ import annotations

from enum import Enum


class AnalysisStatus(Enum):
    ANALYSIS_SUCCEEDED = "Analysis succeeded"
    ANALYSIS_IN_PROGRESS = "Analysis in progress"
    ANALYSIS_FAILED = "Analysis failed"
    ANALYSIS_NOT_FOUND = "NOT FOUND"
    ANALYSIS_ERROR = "ERROR"

    def _get_ordering(self: AnalysisStatus) -> dict[AnalysisStatus, int]:
        return {name: idx for idx, name in enumerate(self.__class__)}

    def __lt__(self: AnalysisStatus, other: AnalysisStatus) -> bool:
        ordering = self._get_ordering()
        return ordering[self] < ordering[other]

    def __gt__(self: AnalysisStatus, other: AnalysisStatus) -> bool:
        ordering = self._get_ordering()
        return ordering[self] > ordering[other]
