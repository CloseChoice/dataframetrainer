from enum import Enum

class ChallengeStatus(Enum):
    UNSEEN = -1
    SEEN = 0
    TRIED = 1
    SOLVED = 2
