def solution(x):
    x_back = x

    total = 0

    x_back = str(x)
    print(x_back)

    for i in range(len(x_back)):
        total += int(x_back[i])
    # if x_back >= 10000:
    #     total += x_back // 10000
    #     x_back = x_back % 10000
    # if x_back >= 1000:
    #     total += x_back // 1000
    #     x_back = x_back % 1000
    # if x_back >= 100:
    #     total += x_back // 100
    #     x_back = x_back % 100
    # if x_back >= 10:
    #     total += x_back // 10
    #     x_back = x_back % 10
    # if x_back >= 1:
    #     total += x_back // 1

    # print(total)


    return True if x%total == 0 else False


print(solution(11))