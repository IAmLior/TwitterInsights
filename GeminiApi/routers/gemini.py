from fastapi import APIRouter, HTTPException, Body
from handlers.gemini import GeminiHandler

gemini_handler = GeminiHandler()


class GeminiRouter:

    router = APIRouter(prefix="/gemini")

    @router.post("/categorize")
    async def categorize(tweets: list[dict] = Body(...)):
        try:
            return await gemini_handler.categorize(tweets)
        except Exception as ex:
            return {"result": str(ex), "status_code": 500}
