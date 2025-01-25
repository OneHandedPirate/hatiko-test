from typing import Annotated, NoReturn

from fastapi import APIRouter, HTTPException, status, Depends

from src.api.schemas import CheckImeiAPISchema, CheckImeiResponseSchema
from src.core.config import settings
from src.api.services.imei_service import (
    ImeiCheckApiService,
    get_imei_api_service,
    ImeiCheckServiceSchema,
)


router = APIRouter()


@router.post("/check-imei", response_model=CheckImeiResponseSchema)
async def check_imei(
    data: CheckImeiAPISchema,
    imei_api_service: Annotated[ImeiCheckApiService, Depends(get_imei_api_service)],
) -> CheckImeiResponseSchema | NoReturn:
    """Проверка IMEI"""
    if data.token != settings.api.token:
        raise HTTPException(
            detail="Invalid token", status_code=status.HTTP_403_FORBIDDEN
        )

    try:
        return await imei_api_service.execute(ImeiCheckServiceSchema(imei=data.imei))
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
