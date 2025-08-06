def solution(maps):
    n = len(maps)
    m = len(maps[0])


    answer = []
    answer_mirror = []


    dx =[-1,1,0,0]
    dy =[0,0,1,-1]

    for i in range(len(maps)):
        for v in range(len(maps)):
            if maps[i][v] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                answer_mirror.append((i,v))
            else:
                answer_mirror.append(False)     

    for x,y in answer_mirror:
        for z in range(4):
            nx = x+dx[z]
            ny = y+dy[z]
            if 0 <= nx < n and 0 <= ny < m :
                if 


    for i in answer_mirror:
        print(i)

    return answer


print(solution
      (["X591X",
      "X1X5X",
      "X231X", 
      "1XXX1"])
      )


# print(solution
#       (["XXXXX",
#       "XXXXX",
#       "XXXXX", 
#       "XXXXX"])
#       )