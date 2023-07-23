from elo.entities.ChallengeElo import ChallengeElo
from elo.entities.UserElo import UserElo

DIVISOR = 400
CUTOFF_PROB = 0.4
IGNORE_LAST_N_CHALLENGES = 5

def calculate_elo(challenge_elo: ChallengeElo, user_elo: UserElo, div: float) -> float:
    prob_success = 1 / (1 + 10 ** ((challenge_elo.elo - user_elo.elo) / div))
    return prob_success

def get_best_suited_challenge(challenges: list[ChallengeElo], user_elo: UserElo, past_challenges: list[str]) -> tuple[str, float]:
    success_probs = {}
    for challenge in challenges:
        if challenge.challenge_id in past_challenges[:IGNORE_LAST_N_CHALLENGES]:
            continue
        success_probs[challenge.challenge_id] = calculate_elo(challenge, user_elo, DIVISOR)
    # We want a success prob of CUTOFF_PROB to be the minimum
    relevant_succes_probs = {name: prob for name, prob in success_probs.items() if prob >= CUTOFF_PROB}
    return list(sorted(relevant_succes_probs.items(), key=lambda x: x[1]))[0]



