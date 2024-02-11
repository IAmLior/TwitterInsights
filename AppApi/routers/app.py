from fastapi import APIRouter, HTTPException
from handlers.app import AppHandler

app_handler = AppHandler()

class AppRouter:

    router = APIRouter(prefix="/app")

    @router.post("/getInsights")
    async def get_insights(tokens: list[str]):
        try:
            app_handler.get_insights(tokens)
        except Exception as ex:
            raise HTTPException(status_code=ex.status_code, detail=ex.detail)