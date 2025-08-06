def solution(board):
    n = len(board) # 행  0 , 1 , 2 ,3  
    m = len(board[0]) # 열 0, 1, 2, 3, 4

    # 원래 1이 있던 위치만 기록
    bomb = []

    for i in range(n):
        for o in range(m):
            if board[i][o] == 1:
                bomb.append((i, o))


    dx = [-1, -1, -1,  0, 0,  1, 1, 1]
    dy = [-1,  0,  1, -1, 1, -1, 0, 1]

    for x,y in bomb:
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                board[nx][ny] = 1 
        print(x,y)
    # 0의 개수 세기
    answer = 0
    for i in range(n):
        for o in range(m):

            if board[i][o] == 0:
                answer += 1
    for i in board:    
        print(i)
    return answer


# 테스트
print(solution([
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 0]
]))
