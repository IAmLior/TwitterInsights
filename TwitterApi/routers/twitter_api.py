from fastapi import APIRouter, HTTPException, Query, status
from handlers.service import Service
from typing import List
import json
from models.post_tweet_request import PostTweetRequest


service = Service()
router = APIRouter()


@router.get("/get_data/")
async def get_data(tokens: List[str] = Query(None)):
    if not tokens:
        raise HTTPException(status_code=400, detail="Tokens are required")

    result = service.fetch(tokens)
    return {"result": result}


@router.post("/post_tweet/")
async def post_tweet(request: PostTweetRequest):
    try:
        response = service.post_tweet(request.text)
        return {"result": response, "status_code": status.HTTP_201_CREATED}
    except Exception as ex:
        return {"result": str(ex), "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR}
