def solution(board):
    n = len(board)
    m = len(board[0])

    # 원래 1이 있던 위치만 기록
    bomb = []

    for i in range(n):
        for o in range(m):
            if board[i][o] == 1:
                bomb.append((i, o))


    # 0의 개수 세기
    answer = 0
    for i in range(n):
        for o in range(m):
            if board[i][o] == 0:
                answer += 1

    return answer


# 테스트
print(solution([
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 0]
]))
