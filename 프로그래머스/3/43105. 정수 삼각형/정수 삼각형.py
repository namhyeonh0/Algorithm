def solution(triangle):
    answer = 0
    for i in range(len(triangle)-1):
        newlevel = []
        for j in range(len(triangle[i])):
            if len(newlevel) == 0:
                newlevel.append(triangle[i][j] +triangle[i+1][j])
                newlevel.append(triangle[i][j] + triangle[i+1][j+1])
            else:
                if newlevel[j] < triangle[i][j] + triangle[i+1][j]:
                    newlevel[j] = triangle[i][j] + triangle[i+1][j]
                newlevel.append(triangle[i][j] + triangle[i+1][j+1])
        triangle[i+1] = newlevel
    answer = max(triangle[-1])
    return answer