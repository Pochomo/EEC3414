#특정 프로젝트가 받은 피드백 점수를 측정하여 개발자의 영향 평가
"""
- 개발자가 진행한 프로젝트가 총 n 개 있다고 할 때
- s 점 이상의 피드백을 받은 프로젝트가 최소 s 개 이상이고 
나머지 프로젝트는 s 점 이하의 피드백을 받아야 합니다.
- 이러한 조건을 만족하는 s중에서 최댓값이 개발자의 영향력 지수(Impact Score)
가 됩니다
"""
def cal_impact():
    a_input.sort(reverse=True)
    #6 5 3 1 0
    impact = 0
    for i in range(len(a_input)-1, -1, -1): #정렬하면 몇개 이상인지 판단 쉽고 인데긋로 평가 하면 됨
        if a_input[i] >= i + 1:
            impact = max(impact, i + 1)
    
    return impact

a_input = list(map(int, input().split()))

print(cal_impact())