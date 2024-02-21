from fastapi import APIRouter, HTTPException
from handlers.gemini import GeminiHandler
from models.gemini import TweetData

gemini_handler = GeminiHandler()

class GeminiRouter:

    router = APIRouter(prefix="/gemini")

    @router.post("/categorize")
    async def categorize(tweets: list[TweetData]):
        try:
            return gemini_handler.categorize(tweets)
        except Exception as ex:
            raise HTTPException(status_code=ex.status_code, detail=ex.detail)