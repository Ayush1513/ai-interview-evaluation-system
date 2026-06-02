from pydantic import BaseModel


class ScoreRequest(BaseModel):

    question: str
    answer: str