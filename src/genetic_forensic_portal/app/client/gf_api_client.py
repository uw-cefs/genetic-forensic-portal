from __future__ import annotations

MISSING_DATA_ERROR = "data is required"


def upload_sample_analysis(data: bytes, metadata: str | None = None) -> str:
    # This is a placeholder. Eventually, the real API call will be here
    # and we can return its response

    if data is None:
        raise ValueError(MISSING_DATA_ERROR)

    sample_identifier = "this-is-a-uuid"

    if metadata is None:
        sample_identifier = "this-is-a-differentuuid"

    return sample_identifier
