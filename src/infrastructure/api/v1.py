from fastapi.routing import APIRouter

from src.infrastructure.api.routers.health_check import health_router
from src.infrastructure.api.routers.work import work_router

router = APIRouter(prefix="/api/v1")
router.include_router(router=health_router)
router.include_router(router=work_router)
