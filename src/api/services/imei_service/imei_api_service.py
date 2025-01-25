import logging

import aiohttp

from src.api.services.imei_service.exceptions import ImeiApiBaseException
from src.api.services.imei_service.schemas import ImeiCheckServiceSchema
from src.core.config import settings


logger = logging.getLogger(__name__)


class ImeiCheckApiService:
    @classmethod
    async def execute(cls, data: ImeiCheckServiceSchema):
        headers = {
            "Authorization": f"Bearer {settings.imei_api.token}",
            "Content-Type": "application/json",
        }

        body = {"deviceId": data.imei, "serviceId": 24}

        try:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=10)
            ) as aiohttp_session:
                res = await aiohttp_session.post(
                    f"{settings.imei_api.url}/v1/checks", headers=headers, json=body
                )

                if res.status != 201:
                    raise ImeiApiBaseException("Некорректный статус ответа от API")

                return await res.json()
        except Exception as e:
            logger.exception(
                "Exception occurred while requesting ImeiCheckApiService: %s",
                str(e),
                exc_info=True,
            )
            raise ImeiApiBaseException()


def get_imei_api_service() -> ImeiCheckApiService:
    return ImeiCheckApiService()
