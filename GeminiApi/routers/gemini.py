from fastapi import APIRouter, HTTPException
from handlers.gemini import GeminiHandler

gemini_handler = GeminiHandler()

class GeminiRouter:

    router = APIRouter(prefix="/gemini")

    @router.get("/categorize")
    async def categorize(text: str):
        try:
            return gemini_handler.categorize(text)
        except Exception as ex:
            raise HTTPException(status_code=ex.status_code, detail=ex.detail)