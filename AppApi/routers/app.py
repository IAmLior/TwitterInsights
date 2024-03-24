from fastapi import APIRouter, HTTPException, Query
from handlers.app import AppHandler
from models.app import PostTweet

app_handler = AppHandler()


class AppRouter:

    router = APIRouter(prefix="/app")

    @router.get("/getInsights/")
    async def get_insights(tokens: list[str] = Query(None)):
        try:
            result = app_handler.get_insights(tokens)
            return {"result": result}
        except Exception as ex:
            raise HTTPException(status_code=500, detail=ex)

    @router.post("/postTweet")
    async def post_tweet(text: str):
        try:
            result = app_handler.post_tweet(text)
            print(result)
            return {"result": result}
        except Exception as ex:
            raise HTTPException(status_code=500, detail=ex)
