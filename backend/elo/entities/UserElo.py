from pydantic import BaseModel

class UserElo(BaseModel):
    elo: float
    user_id: str