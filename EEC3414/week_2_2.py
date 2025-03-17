def MySort(arr):
    for i in range(len(arr) -1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]; 
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

# 첫 번째 줄에서 n 을 입력받음
n = int(input())
# 띄어쓰기로 구분된 정수를 입력받음
numbers = list(map(int, input().split()))
# 정렬을 실행
sorted_numbers = MySort(numbers)
# 정렬된 결과를 띄어쓰기로 구분하여 출력
print(' '.join(map(str, sorted_numbers)))