def solution(participant, completion):
    player_dict = {}

    for e in participant:
        player_dict[e] = player_dict.get(e, 0) + 1
    
    for e in completion:
        player_dict[e] -= 1

    for k, v in player_dict.items():
        if v == 1:
            return k    


print(solution(['leo', 'kiki', 'eden' ], ['eden', 'kiki']))
print(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']))
print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))