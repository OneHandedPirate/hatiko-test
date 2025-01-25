def validate_imei(imei: str) -> bool:
    return imei.isdigit() and len(imei) == 15
