def solution(babbling):
    
    list = []
    list.append(["aya","ye","woo","ma"])

    answer = 0
    
    for i in range(len(babbling)):
        list = babbling[i].replace(list, "")

    return answer


#print(solution(["aya", "yee", "u", "maa", "wyeoo"])) #return 1
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))	#return3