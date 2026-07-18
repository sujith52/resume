from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="AI Resume Screening Agent",
    description="API for ranking resumes against job descriptions",
    version="1.0"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Resume Screening API is running"
    }