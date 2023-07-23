from pydantic import BaseModel

class ChallengeElo(BaseModel):
    elo: float
    challenge_id: str
