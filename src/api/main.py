from fastapi import FastAPI, APIRouter

from src.core.config import settings
from src.api.router import router as check_router


app: FastAPI = FastAPI(
    title="IMEI Check API",
    description="App to check IMEI",
)

main_router = APIRouter(prefix="/api")
main_router.include_router(check_router)
app.include_router(main_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.api.host, port=settings.api.port)
