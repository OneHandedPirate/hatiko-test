class ImeiApiBaseException(Exception):
    def __init__(self, message: str = "Произошла ошибка в IMEI API Service"):
        super().__init__(message)
