def solution(m, n, board):
    answer = 0
    boardList = [[char for char in string] for string in board]
    
    while True:
        check = find4s(boardList)
        answer += len(check[0])
        if len(check[0]) == 0:
            break
        
    return answer

def find4s(boardList):
    
    check4s = []
    for i in range(len(boardList)-1):
        for j in range(len(boardList[0])-1):
            now = boardList[i][j]
            if now != " " and boardList[i][j+1] == now and boardList[i+1][j] == now and boardList[i+1][j+1] == now:
                check4s.append([i,j])
                check4s.append([i,j+1])
                check4s.append([i+1,j])
                check4s.append([i+1,j+1])
                
    check4s_done = []
    for pair in check4s:
        if pair not in check4s_done:
            check4s_done.append(pair)
    
    for pair in check4s_done:
        boardList[pair[0]][pair[1]] = " "
        
    for i in range(len(boardList)-1,0,-1):
        for j in range(len(boardList[0])):
            for count in range(i):
                if boardList[i][j] == " ":
                    for k in range(i,0,-1):
                        boardList[k][j] = boardList[k-1][j]
                    boardList[0][j] = " "
                    
    return check4s_done, boardList