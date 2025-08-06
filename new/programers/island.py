import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    n = len(maps)
    m = len(maps[0])


    answer = []
    visited = set()


    dx =[-1,1,0,0]
    dy =[0,0,1,-1]

    def dfs(x,y):
        if (x,y) in visited or maps[x][y] == "X":
            return 0
        visited.add((x,y))
        total = int(maps[x][y])

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                total += dfs(nx, ny)

        return total

    for i in range(n):
        for v in range(m):
            if (i,v) not in visited and maps[i][v] !="X":
                answer.append(dfs(i,v))


    return sorted(answer) if answer else [-1]


# print(solution
#       (["X591X",
#       "X1X5X",
#       "X231X", 
#       "1XXX1"])
#       )


print(solution
      (["XXXXX",
      "XXXXX",
      "XXXXX", 
      "XXXXX"])
      )