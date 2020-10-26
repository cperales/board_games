import numpy as np
import random

# Maximum of 10 players
max_players = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
]

s_players_round = {
    1: 2,
    2: 3,
    3: 3,
    4: 4,
    5: 3,
}


def make_proposal(players, s):
    proposal = random.sample(players, k=s)
    return proposal


def vote_proposal(players, proposal):
    vote_result = 0
    for p in players:
        vote = random.randint(0, 1)
        print(p, vote)
        vote_result += vote
    if vote_result < 3:
        return True
    else:
        return False


def mission_result(selected_players,
                   evil_players,
                   prob_sab):
    mission = 0
    for p in selected_players:
        if p in evil_players:
            if np.random.choice([0, 1], p=[1 - prob_sab,
                                           prob_sab]) == 1:
                print('Evil player', p, 'sabotaged!')
                mission = 1
    return mission


def round(r, players, evil_players, prob_sab):
    s = s_players_round[r]
    print('Round', r, ', selected', s, 'players')
    accepted = False
    while accepted is False:
        proposal = make_proposal(players, s)
        print('Proposal is', proposal)
        accepted = vote_proposal(players, proposal)
        if accepted is False:
            print('Proposal is denied')
        else:
            print('Proposal is accepted')
    selected_players = proposal
    mission = mission_result(selected_players,
                             evil_players,
                             prob_sab)
    if mission == 0:
        print('Mission passed')
    else:
        print('Mission sabotaged')
    return mission


def match(N, e, prob_sab):
    players = max_players[:N]
    print(N, 'players in this match,', players)
    evil_players = random.sample(players, k=e)
    print('Evil players are', evil_players)

    count_match = 0
    for r in range(1, 5 + 1):
        count_match += round(r, players, evil_players, prob_sab)
        print()

    if count_match < 3:
        print('Good players win!')
        match_result = 0
    else:
        print('Bad players win!')
        match_result = 1

    return match_result


if __name__ == '__main__':
    # Players to play this match
    N = 6
    # Evil players
    e = 2
    # Probability of sabotage
    prob = 1
    # Game
    match(N, e, prob_sab=prob)
