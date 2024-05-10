from __future__ import annotations

from pathlib import Path

from genetic_forensic_portal.utils.analysis_status import AnalysisStatus

MISSING_DATA_ERROR = "data is required"
MISSING_UUID_ERROR = "uuid is required"

SAMPLE_UUID = "this-is-a-uuid"
NO_METADATA_UUID = "this-is-a-differentuuid"
NOT_FOUND_UUID = "not-found-uuid"
NOT_AUTHORIZED_UUID = "not-authorized-uuid"
IN_PROGRESS_UUID = "in-progress-uuid"
ANALYSIS_FAILED_UUID = "failed-uuid"

UUID_LIST = [
    SAMPLE_UUID,
    NO_METADATA_UUID,
    NOT_FOUND_UUID,
    NOT_AUTHORIZED_UUID,
    IN_PROGRESS_UUID,
    ANALYSIS_FAILED_UUID,
]

SAMPLE_IMAGE_PATH = (
    Path(__file__).parents[2] / "resources" / "sample_images"
)  # equivalent to ../../resources/sample_images
SCAT_SAMPLE_IMAGE = str(SAMPLE_IMAGE_PATH / "tan001_scat.png")
SCAT_SAMPLE_IMAGE_2 = str(SAMPLE_IMAGE_PATH / "tan002_scat.png")

# Add Voronoi sample image paths
VORONOI_SAMPLE_IMAGE = str(SAMPLE_IMAGE_PATH / "tan001_voronoi.png")
VORONOI_SAMPLE_IMAGE_2 = str(SAMPLE_IMAGE_PATH / "tan002_voronoi.png")


def upload_sample_analysis(data: bytes, metadata: str | None = None) -> str:
    """Uploads a sample analysis from the web portal to the API

    Args:
        data (bytes): The data to upload
        metadata (str | None): The metadata to upload"""
    # This is a placeholder. Eventually, the real API call will be here
    # and we can return its response

    if data is None:
        raise ValueError(MISSING_DATA_ERROR)

    sample_identifier = SAMPLE_UUID

    if metadata is None:
        sample_identifier = NO_METADATA_UUID

    return sample_identifier


def get_scat_analysis(sample_id: str) -> str:
    """Gets the SCAT analysis for a sample

    Args:
        sample_id (str): The sample ID to get the SCAT analysis for"""
    # This is a placeholder. Eventually, the real API call will be here
    # and we can return its response

    if sample_id is None:
        raise ValueError(MISSING_UUID_ERROR)

    analysis = None

    if sample_id == SAMPLE_UUID:
        analysis = SCAT_SAMPLE_IMAGE
    elif sample_id == NO_METADATA_UUID:
        analysis = SCAT_SAMPLE_IMAGE_2
    elif sample_id == IN_PROGRESS_UUID:
        analysis = SCAT_SAMPLE_IMAGE  # This can be any image that represents an in-progress state

    if analysis is None:
        raise FileNotFoundError

    return analysis


def get_voronoi_analysis(sample_id: str) -> str:
    """Gets the Voronoi analysis for a sample

    Args:
        sample_id (str): The sample ID to get the Voronoi analysis for"""

    if sample_id is None:
        raise ValueError(MISSING_UUID_ERROR)

    analysis = None

    if sample_id == SAMPLE_UUID:
        analysis = VORONOI_SAMPLE_IMAGE
    elif sample_id == NO_METADATA_UUID:
        analysis = VORONOI_SAMPLE_IMAGE_2

    if analysis is None:
        raise FileNotFoundError

    return analysis


def list_analyses() -> list[str]:
    """Lists UUIDs for all SCAT analyses

    Returns:
        list[str]: A list of all SCAT analyses"""
    # This is a placeholder. Eventually, the real API call will be here
    # and we can return its response

    return UUID_LIST


def get_analysis_status(sample_id: str) -> str:
    """
    Retrieves the status of the analysis based on the given UUID.

    Args:
        sample_id (str): The UUID of the analysis to retrieve the status for.

    Returns:
        str: The human-readable status of the analysis.

    """
    if sample_id is None:
        raise ValueError(MISSING_UUID_ERROR)

    if sample_id in [SAMPLE_UUID, NO_METADATA_UUID]:
        return AnalysisStatus.ANALYSIS_SUCCEEDED.value
    if sample_id == IN_PROGRESS_UUID:
        return AnalysisStatus.ANALYSIS_IN_PROGRESS.value
    if sample_id == ANALYSIS_FAILED_UUID:
        return AnalysisStatus.ANALYSIS_FAILED.value

    error_message = "No analysis found for the given UUID"
    raise FileNotFoundError(error_message)
