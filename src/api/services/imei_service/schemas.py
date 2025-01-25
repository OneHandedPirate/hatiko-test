from pydantic import BaseModel, field_validator


class ImeiCheckServiceSchema(BaseModel):
    imei: str

    @field_validator("imei")
    @classmethod
    def validate_imei(cls, value):
        if not value.isdigit():
            raise ValueError("IMEI должен состоять только из цифр")
        if len(value) != 15:
            raise ValueError("IMEI должен содержать ровно 15 символов")
        return value
