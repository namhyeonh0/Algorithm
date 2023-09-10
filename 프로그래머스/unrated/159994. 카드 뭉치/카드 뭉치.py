def solution(cards1, cards2, goal):
    answer = []
    n = len(goal)
    for i in range(n):
        if len(cards1) != 0 and goal[0] == cards1[0]:
            cards1.remove(cards1[0])
            goal.remove(goal[0])
        elif len(cards2) != 0 and goal[0] == cards2[0]:
            cards2.remove(cards2[0])
            goal.remove(goal[0])
    if len(goal) == 0:
        answer = 'Yes'
    else:
        answer = 'No'
    return answer