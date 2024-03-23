from pydantic import BaseModel


class TweetData(BaseModel):
    author: str
    text: str
