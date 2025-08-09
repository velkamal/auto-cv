from fastapi import FastAPI

from autocv.api.routes import router
from autocv.config import settings

app = FastAPI(title=settings.app_name)
app.include_router(router)


@app.get("/", summary="Health check")
async def root() -> dict[str, str]:
    """Simple endpoint for health checks."""
    return {"status": "ok"}
