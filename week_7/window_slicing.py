#문자열 s와 t의 window substring 이란, s의 어떤 연속된 부분 문자열 중 t에 포함된 모든 문자(중복 포함)가 포함된 문자열을 뜻한다.
# 길이가 각각 m, n인 문자열 s와 t가 주어졌을 때, s와 t의 window substring 중 가장 짧
# 은 문자열을 출력하라.
def window_substring(s, t):
    if len(s) < len(t):
        return ""
    
    # 문자의 빈도 수 저장 하는 딕셔너리 키 벨류로 저장장
    freq = {}
    for char in t:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # 문자의 수수
    cnt = len(freq)
    # 조건 만족한 수
    formed = 0
    
    l = 0
    # 최소 길이
    shortest = len(s) + 1
    # 시작 끝 인덱스
    start, end = -1, -1
    
    # 오른쪽 포인터를 이동 시킨다.
    for r in range(len(s)):
        if s[r] in freq:
            # 문자 찾아서 해당 문자 갯수 감소
            freq[s[r]] -= 1
            # 빈도수 만족 하면
            if freq[s[r]] == 0:
                formed += 1
        
        while l <= r and formed == cnt:
            if r - l + 1 < shortest:
                shortest = r - l + 1
                start, end = l, r
            
            if s[l] in freq:
                # 왼쪽 문자 제거 필요한 개수 만큼 있으면 조건 불만족이다.
                if freq[s[l]] == 0:
                    formed -= 1
                # 다시 필요한 개수 만큼 증가시킨다.
                freq[s[l]] += 1
            
            #왼쪽 포인터 이동동
            l += 1
    # 못찾으면 빈 문자열 반환환
    if start == -1:
        return ""
    else:
        return s[start:end+1]

s = input()
t = input()
print(window_substring(s, t))