from pydantic import BaseModel


class TurnRequest(BaseModel):
    state: bool
