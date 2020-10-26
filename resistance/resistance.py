import numpy as np
import matplotlib.pyplot as plt
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

# Players to play this match
N = 6
# Evil players
e = 2
# Probability of sabotage
prob = 1
players = max_players[:6]
print(N, 'players in this match,', players)
evil_players = random.sample(players, k=e)
print('Evil players are', evil_players)

s_players_round = {
    1: 2,
    2: 3,
    3: 3,
    4: 4,
    5: 3,
}


def make_proposal(s):
    proposal = random.sample(players, k=s)
    return proposal


def vote_proposal(proposal):
    vote_result = 0
    for p in players:
        vote = random.randint(0, 1)
        print(p, vote)
        vote_result += vote
    if vote_result < 3:
        return True
    else:
        return False


def mission_result(selected_players):
    mission = 0
    for p in selected_players:
        if p in evil_players:
            if np.random.choice([0, 1], p=[1 - prob, prob]) == 1:
                print('Evil player', p, 'sabotaged!')
                mission = 1
    return mission


def round(r):
    s = s_players_round[r]
    print('Round', r, ', selected', s, 'players')
    accepted_proposal = False
    while accepted_proposal is False:
        proposal = make_proposal(s)
        print('Proposal is', proposal)
        accepted_proposal = vote_proposal(proposal)
        if accepted_proposal is False:
            print('Proposal is denied')
        else:
            print('Proposal is accepted')
    selected_players = proposal
    mission = mission_result(selected_players)
    if mission == 0:
        print('Mission passed')
    else:
        print('Mission sabotaged')
    return mission


match = 0
for r in [1, 2, 3, 4, 5]:
    match += round(r)
    print()

if match < 3:
    print('Good players win!')
else:
    print('Bad players win!')
