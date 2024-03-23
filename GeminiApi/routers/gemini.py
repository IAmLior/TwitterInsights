from fastapi import APIRouter, HTTPException, Body
from handlers.gemini import GeminiHandler
from models.gemini import TweetData

gemini_handler = GeminiHandler()


class GeminiRouter:

    router = APIRouter(prefix="/gemini")

    @router.post("/categorize")
    async def categorize(tweets: list[dict] = Body(...)):
        try:
            return gemini_handler.categorize(tweets)
        except Exception as ex:
            print(f"########## {ex}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
