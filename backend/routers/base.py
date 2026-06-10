from fastapi.routing import APIRouter

from .airport import airport_router

base_router = APIRouter(prefix="/api/v1")
print(123)
base_router.include_router(airport_router)
