def solution(X, Y):
    a = []
    b = []
    c = []

    a.append(X)
    b.append(Y)

    r = list(a[0])
    s = list(b[0])

    for ch in r:
        if ch in s:
            c.append(ch)
            s.remove(ch)
            print("ch의 값", ch)
    v = ''.join(c)

    print("v의 값", v)
    if v == "":
        v = "-1"

    if v == "-1":
        str_answer = "-1"
        print(f'"{str_answer}"')
    else:
        o = sorted(v, reverse=True)
        ''.join(o)
        answer = ''.join(o)
        str_answer = str(answer)
        if str_answer[0] == '0':
            str_answer ='0'
        print(f'"{str_answer}"')

    return str_answer


#solution("100","2345") # 결과값 -1
#solution("12321","42531") # 결과값 321
#solution("5525","1255") # 결과값 552
solution("100","203045") # 결과값 0
 