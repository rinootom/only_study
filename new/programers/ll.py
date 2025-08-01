def solution(s):
    coin = 0 
    for ch in s:
        if ch == "(":
            coin += 1
        elif ch == ")":
            coin -= 1
            if coin < 0:
                return False  
    return coin == 0  


print(solution("(())()"))  # True
print(solution("(()("))    # False