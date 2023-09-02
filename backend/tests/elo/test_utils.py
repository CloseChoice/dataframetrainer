from elo.entities.ChallengeElo import ChallengeElo
from elo.entities.UserElo import UserElo
from elo.utils import get_best_suited_challenge, calculate_elo_update

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

def test_calculate_elo_update():
    challenge_elo = ChallengeElo(elo=2077, challenge_id="2")
    user_elo = UserElo(elo=2306, user_id="1")
    new_challenge_elo, new_user_elo = calculate_elo_update(challenge_elo, user_elo, success=True)
    assert new_challenge_elo.elo == 2076.5777741364204
    assert new_user_elo.elo == 2312.755613817275

    new_challenge_elo, new_user_elo = calculate_elo_update(challenge_elo, user_elo, success=False)
    assert new_challenge_elo.elo == 2078.5777741364204
    assert new_user_elo.elo == 2280.755613817275

