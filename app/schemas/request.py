from pydantic import BaseModel


class ScreeningRequest(BaseModel):

    resume_folder: str
    jd_path: str