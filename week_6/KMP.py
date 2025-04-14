def initnext(p):
    M = len(p)
    next = [0] * M
    next[0] = -1

    j = -1
    
    for i in range(M):
        next[i] = j
        while (j >= 0) and (p[i] != p[j]):
            j = next[j]
        i += 1
        j += 1
    return next

    
def kmp(t, p):
    M = len(p)
    N = len(t)
    next = initnext(p)
    
    i = 0
    j = 0
    result = []
    
    for i in range(N):
        while (j >= 0) and (t[i] != p[j]):
            j = next[j]
            
        i += 1
        j += 1
        
        if j == M:
            result.append(i - M)  # 시작 위치 저장
            j = next[j-1]  # 다음 검색을 위해 j 조정
    
    return result


t = input()
p = input()

cnt = 0
result = kmp(t, p)
# 문자열 T에서 문자열P가 몇 번 나타 나는지
print(len(result))
# 문자열 T에서 문자열 P가 나타나는 위치를 차례대로 공백으로 구분해서 출력
print(' '.join(map(str, [i + 1 for i in result])))