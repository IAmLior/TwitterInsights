from fastapi import APIRouter, HTTPException, Query
from handlers.service import Service
from typing import List
import json


service = Service()
router = APIRouter()


@router.get("/get_data/")
async def get_data(tokens: List[str] = Query(None)):
    if not tokens:
        raise HTTPException(status_code=400, detail="Tokens are required")

    result = service.fetch(tokens)
    return {"result": result}


@router.post("/post_tweet/")
async def post_tweet(text: str):
    return service.post_tweet(text)
