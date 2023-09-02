from elo.entities.ChallengeElo import ChallengeElo
from elo.entities.UserElo import UserElo
from entities.ChallengeStatus import ChallengeStatus

DIVISOR = 400
CUTOFF_PROB = 0.4
IGNORE_LAST_N_CHALLENGES = 5
K_FACTOR_USER = 32
K_FACTOR_CHALLENGE = 2

def calculate_elo(challenge_elo: ChallengeElo, user_elo: UserElo, div: float) -> float:
    prob_success = 1 / (1 + 10 ** ((challenge_elo.elo - user_elo.elo) / div))
    return prob_success

def get_random_challenge(challenges: list[ChallengeElo]) -> str:
    from random import choice
    return choice(challenges).challenge_id

def get_best_suited_challenge(challenges: list[ChallengeElo], user_elo: UserElo, past_challenges: list[str]) -> tuple[str, float]:
    success_probs = {}
    for challenge in challenges:
        if challenge.challenge_id in past_challenges[:IGNORE_LAST_N_CHALLENGES]:
            continue
        success_probs[challenge.challenge_id] = calculate_elo(challenge, user_elo, DIVISOR)
    # We want a success prob of CUTOFF_PROB to be the minimum
    relevant_succes_probs = {name: prob for name, prob in success_probs.items() if prob >= CUTOFF_PROB}
    return list(sorted(relevant_succes_probs.items(), key=lambda x: x[1]))[0]


def calculate_elo_update(challenge: ChallengeElo, user: UserElo, success: bool) -> tuple[ChallengeElo, UserElo]:
    prob_success_user = calculate_elo(challenge, user, DIVISOR)
    prob_success_challenge = 1 - prob_success_user
    new_elo_user = user.elo + K_FACTOR_USER * ((1 if success else 0) - prob_success_user)
    new_elo_challenge = challenge.elo + K_FACTOR_CHALLENGE * ((1 if not success else 0) - prob_success_challenge)
    return ChallengeElo(challenge_id=challenge.challenge_id, elo=new_elo_challenge), UserElo(user_id=user.user_id, elo=new_elo_user)

# todo: add type for conn
def handle_elo_update(challenge_id: str, user_id: str, success: bool, conn) -> None:
    with conn.cursor() as cursor:
        # get data
        print(f"This is the user_id: {user_id} and the challenge_id: {challenge_id}")
        cursor.execute("SELECT status from users_challenges_status WHERE user_id = %s AND challenge_id = %s", (user_id, challenge_id))
        match (fetch_result := cursor.fetchone()):
            case None:
                status = ChallengeStatus(0)
            case (status,):
                status = ChallengeStatus(status)
            case _:
                raise ValueError(f"Expected either tuple or None, got {type(fetch_result)} with values: {fetch_result}")
        # no updates if the challenge was already solved
        if status == ChallengeStatus.SOLVED:
            return
        cursor.execute("SELECT elo FROM challenges_elo WHERE challenge_id = %s", (challenge_id,))
        elo = cursor.fetchone()
        challenge = ChallengeElo(challenge_id=challenge_id, elo=elo[0])
        cursor.execute("SELECT elo FROM users_elo WHERE user_id = %s", (user_id,))
        elo = cursor.fetchone()
        user = UserElo(user_id=user_id, elo=elo[0])

        # calculate new elos
        new_challenge_elo, new_user_elo = calculate_elo_update(challenge, user, success)

        # make updates
        cursor.execute("UPDATE challenges_elo SET elo = %s WHERE challenge_id = %s", (new_challenge_elo.elo, new_challenge_elo.challenge_id))
        cursor.execute("UPDATE users_elo SET elo = %s WHERE user_id = %s", (new_user_elo.elo, new_user_elo.user_id))
        conn.commit()
    


