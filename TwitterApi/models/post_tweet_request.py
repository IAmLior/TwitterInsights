from pydantic import BaseModel


class PostTweetRequest(BaseModel):
    text: str
