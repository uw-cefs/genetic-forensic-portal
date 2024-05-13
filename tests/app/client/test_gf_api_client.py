from __future__ import annotations

import pandas as pd
import pytest

import genetic_forensic_portal.app.client.gf_api_client as client
from genetic_forensic_portal.utils.analysis_status import AnalysisStatus

TEST_FILE_DATA = b"this is a file"
TEST_METADATA = "this is metadata"


def test_upload_file_returns_uuid():
    response = client.upload_sample_analysis(TEST_FILE_DATA, TEST_METADATA)

    assert response == client.SAMPLE_UUID


def test_upload_nothing_returns_error():
    with pytest.raises(ValueError, match=client.MISSING_DATA_ERROR):
        client.upload_sample_analysis(None)  # type: ignore[arg-type]


def test_upload_no_metadata_returns_different_uuid():
    response = client.upload_sample_analysis(TEST_FILE_DATA)

    assert response == client.NO_METADATA_UUID


# SCAT Analysis


def test_get_scat_analysis_returns_image_path():
    response = client.get_scat_analysis(client.SAMPLE_UUID)

    assert response == client.SCAT_SAMPLE_IMAGE


def test_get_scat_analysis_returns_image_path_in_progress_uiud():
    response = client.get_scat_analysis(client.IN_PROGRESS_UUID)

    assert response == client.SCAT_SAMPLE_IMAGE


def test_get_scat_analysis_no_metadata_returns_different_image_path():
    response = client.get_scat_analysis(client.NO_METADATA_UUID)

    assert response == client.SCAT_SAMPLE_IMAGE_2


def test_get_scat_analysis_raises_error():
    with pytest.raises(FileNotFoundError):
        client.get_scat_analysis("not-an-uuid")


def test_get_scat_analysis_raises_error_for_none():
    with pytest.raises(ValueError, match=client.MISSING_UUID_ERROR):
        client.get_scat_analysis(None)  # type: ignore[arg-type]


def test_list_analyses_returns_list():
    response = client.list_analyses()

    assert response == client.UUID_LIST


# Voronoi Analysis


def test_get_voronoi_analysis_returns_image_path():
    response = client.get_voronoi_analysis(client.SAMPLE_UUID)

    assert response == client.VORONOI_SAMPLE_IMAGE


def test_get_voronoi_analysis_no_metadata_returns_different_image_path():
    response = client.get_voronoi_analysis(client.NO_METADATA_UUID)

    assert response == client.VORONOI_SAMPLE_IMAGE_2


def test_get_voronoi_analysis_raises_error():
    with pytest.raises(FileNotFoundError):
        client.get_voronoi_analysis("not-an-uuid")


def test_get_voronoi_analysis_raises_error_for_none():
    with pytest.raises(ValueError, match=client.MISSING_UUID_ERROR):
        client.get_voronoi_analysis(None)  # type: ignore[arg-type]


# Tests for the get_analysis_status function
def test_get_analysis_status_succeeded():
    response = client.get_analysis_status(client.SAMPLE_UUID)
    assert response == AnalysisStatus.ANALYSIS_SUCCEEDED.value


def test_get_analysis_status_in_progress():
    response = client.get_analysis_status(client.IN_PROGRESS_UUID)
    assert response == AnalysisStatus.ANALYSIS_IN_PROGRESS.value


def test_get_analysis_status_failed():
    response = client.get_analysis_status(client.ANALYSIS_FAILED_UUID)
    assert response == AnalysisStatus.ANALYSIS_FAILED.value


def test_get_analysis_status_not_found():
    with pytest.raises(FileNotFoundError):
        client.get_analysis_status("unknown-uuid")


def test_get_analysis_status_no_uuid_provided():
    with pytest.raises(ValueError, match=client.MISSING_UUID_ERROR):
        client.get_analysis_status(None)  # type: ignore[arg-type]


# Familial Analysis


def test_get_familial_analysis_returns_image_path():
    response = client.get_familial_analysis(client.SAMPLE_UUID)

    pd.testing.assert_frame_equal(
        response, pd.read_csv(client.FAMILIAL_SAMPLE_DATA, sep="\t", skiprows=1)
    )


def test_get_familial_analysis_no_metadata_returns_different_image_path():
    response = client.get_familial_analysis(client.NO_METADATA_UUID)

    pd.testing.assert_frame_equal(
        response, pd.read_csv(client.FAMILIAL_SAMPLE_DATA_2, sep="\t", skiprows=1)
    )


def test_get_familial_analysis_raises_error():
    with pytest.raises(FileNotFoundError):
        client.get_familial_analysis("not-an-uuid")


def test_get_familial_analysis_raises_error_for_none():
    with pytest.raises(ValueError, match=client.MISSING_UUID_ERROR):
        client.get_familial_analysis(None)  # type: ignore[arg-type]


def test_get_familial_analysis_with_erroring_file_raises():
    with pytest.raises(RuntimeError, match=client.FAMILIAL_TSV_ERROR):
        client.get_familial_analysis(client.FAMILIAL_FILE_PARSE_ERROR_UUID)
