def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        print("True")
        return True
    else:
        print("False")
        return False



# solution("pPoooyY")
solution("Pyy")