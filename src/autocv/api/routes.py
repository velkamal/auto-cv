from fastapi import APIRouter

from autocv.models.schemas import CVRequest
from autocv.services.cv_generator import generate_cv

router = APIRouter(prefix="/api", tags=["cv"])


@router.post("/generate-cv", summary="Generate CV")
async def create_cv(payload: CVRequest) -> dict[str, str]:
    """Generate an ATS-friendly CV.

    This endpoint accepts CV data and returns the path to the generated document.
    """
    file_path = generate_cv(payload)
    return {"file_path": file_path}
