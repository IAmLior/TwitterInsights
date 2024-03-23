from fastapi import APIRouter, HTTPException
from handlers.app import AppHandler

app_handler = AppHandler()


class AppRouter:

    router = APIRouter(prefix="/app")

    @router.post("/getInsights")
    async def get_insights(tokens: list[str]):
        try:
            result = app_handler.get_insights(tokens)
            return {"result": result}
        except Exception as ex:
            raise HTTPException(status_code=500, detail=ex)
