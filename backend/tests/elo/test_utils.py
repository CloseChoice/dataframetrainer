from elo.entities.ChallengeElo import ChallengeElo
from elo.entities.UserElo import UserElo
from elo.utils import get_best_suited_challenge

def test_get_best_suited_challenge():
    challenges = [
        ChallengeElo(elo=1000, challenge_id="1"),
        ChallengeElo(elo=2000, challenge_id="2"),
        ChallengeElo(elo=3000, challenge_id="3"),
        ChallengeElo(elo=4000, challenge_id="4"),
    ]
    user_elo = UserElo(elo=2000, user_id="1")
    assert get_best_suited_challenge(challenges, user_elo, past_challenges=[]) == ("2", 0.5)


def test_get_best_suited_challenge_slightly_above_40():
    challenges = [
        ChallengeElo(elo=1200, challenge_id="1"),
        ChallengeElo(elo=1400, challenge_id="2"),
        ChallengeElo(elo=1600, challenge_id="3"),
        ChallengeElo(elo=1770, challenge_id="4"),
    ]
    user_elo = UserElo(elo=1700, user_id="1")
    d = get_best_suited_challenge(challenges, user_elo, past_challenges=[])
    assert d == ("4", 0.40060320329074317)


def test_get_best_suited_challenge_ignore():
    challenges = [
        ChallengeElo(elo=1200, challenge_id="1"),
        ChallengeElo(elo=1400, challenge_id="2"),
        ChallengeElo(elo=1600, challenge_id="3"),
        ChallengeElo(elo=1770, challenge_id="4"),
    ]
    user_elo = UserElo(elo=1700, user_id="1")
    d = get_best_suited_challenge(challenges, user_elo, past_challenges=["1", "4"])
    assert d == ("3", 0.6400649998028851)
