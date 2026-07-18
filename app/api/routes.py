from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.schemas.request import ScreeningRequest
from app.services.screening_service import screen_all_resumes


router = APIRouter()


@router.post("/screen")
def screen_resumes(request: ScreeningRequest):

    resume_folder = Path(
        request.resume_folder
    )

    jd_path = Path(
        request.jd_path
    )


    # Validate resume folder
    if not resume_folder.exists():
        raise HTTPException(
            status_code=404,
            detail="Resume folder not found"
        )


    # Validate JD file
    if not jd_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Job description file not found"
        )


    try:

        candidates = screen_all_resumes(
            resume_folder,
            jd_path
        )


        return {
            "total_candidates": len(candidates),
            "results": candidates
        }


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )