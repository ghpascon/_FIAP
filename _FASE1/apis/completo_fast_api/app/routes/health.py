from fastapi import APIRouter,Depends
from app.schemas.health import HealthResponse

router = APIRouter(prefix="/health", tags=["HEALTH"])

@router.get(
    "/",
    responses={
        200:{'model':HealthResponse}
        },
    summary="Verifica o estado da API",
    tags=["HEALTH"]
)
def health_check():
    return {"status": "ok"}
