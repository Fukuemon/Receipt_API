from fastapi import APIRouter

router = APIRouter()


@router.get("/health_check")
async def handle_health_check() -> dict:
    return {"status": "ok"}
