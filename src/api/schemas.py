from typing import Optional

from pydantic import BaseModel, field_validator


class CheckImeiAPISchema(BaseModel):
    imei: str
    token: str

    @field_validator("imei")
    @classmethod
    def validate_imei(cls, value):
        if not value.isdigit():
            raise ValueError("IMEI должен состоять только из цифр")
        if len(value) != 15:
            raise ValueError("IMEI должен содержать ровно 15 символов")
        return value


class ServiceSchema(BaseModel):
    id: int
    title: str


class PropertiesSchema(BaseModel):
    deviceName: str
    imei: str
    modelDesc: str
    purchaseCountry: str


class CheckImeiResponseSchema(BaseModel):
    id: str
    type: str
    status: str
    orderId: Optional[str] = None
    service: ServiceSchema
    amount: str
    deviceId: str
    processedAt: int
    properties: PropertiesSchema
