from fastapi.routing import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse

from dependencies import get_point_import_service,PointImportService
from schemas.airport import Airport

import logging

logger = logging.getLogger(__name__)

airport_router = APIRouter(prefix="/airports", tags=["airports"])


@airport_router.post("/import/")
async def import_airport(
    list:list[Airport],
    point_import_service:PointImportService = Depends(get_point_import_service)
):
    logger.info("123")
    try:
        result, failed = point_import_service.import_airport(list=list)
    
        return JSONResponse(content={
            "result":result,
            "failed":failed
        })
    except Exception as e:
        logger.error("An error occurred", exc_info=True)
        return JSONResponse(status_code=500, content={
            "error":{"error"},
        })

@airport_router.get("/{id}/info")
async def get_airport_info():
    pass
