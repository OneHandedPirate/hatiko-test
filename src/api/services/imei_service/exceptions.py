class ImeiApiBaseException(Exception):
    def __init__(self, message: str = "‼ Произошла ошибка при обработке IMEI ‼"):
        super().__init__(message)

class InvalidImei(ImeiApiBaseException):
    pass