from pydantic import BaseModel


class PostTweet(BaseModel):
    text: str
