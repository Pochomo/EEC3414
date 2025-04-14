#이진탐색 구현
import sys
input = sys.stdin.readline

n = int(input())
arr = []
arr = sorted(list(map(int, input().split())))
m = int(input())
check_list = []
check_list = list(map(int, input().split()))

#이진 탐색으로 풀어야함
result = []
for check in check_list:
    start = 0
    end = len(arr) - 1
    found = False
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == check:
            found = True
            break
        elif arr[mid] > check:
            end = mid - 1
        else:
            start = mid + 1
    
    if found:
        result.append(1)
    else:
        result.append(0)

print(*result)

