import random
import time
# 데이타 시각화를 위한 라이브러리, 배우지 않은 라이브러리라 구글 서칭 후 사용했습니다.
import matplotlib.pyplot as plt 

'''MergeSort를 위한 함수 모음'''
# mergesort의 핵심 요소 중 하나인 list를 합치는 함수
def merge(left, right):
    result = []

    i, j = 0, 0
    # left, right 모두 리스트 요소가 남아있을 때 까지 반복한다.
    while i < len(left) and j < len(right):
        # 왼쪽 리스트가 더 작으면 result에 left[i]를 append 한다.
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 왼쪽이 먼저 다 append 되면 right의 남은 요소가 추가된다. 반대는 반대로 추가된다.
    while i < len(left):
        result.append(left[i])
        i += 1
        
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def mergeSort(arr):
    # 리스트의 길이가 1 이하면 이미 정렬이 끝난 것이다.
    if len(arr) <= 1:
        return arr
    
    # 중간을 기준으로 left right를 나눈다.
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 재귀를 활용해 계속 나눈다.
    left = mergeSort(left)
    right = mergeSort(right)

    # merge 함수를 활용해 정렬 한 후 반환
    return merge(left, right)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''QuickSort를 위한 함수'''
# 최대한 arr 안의 mid 값을 뽑기 위해 random으로 3개 뽑아서 그 중 pivot을 설정해 맨 끝에 두는 방식으로 코드를 구현했다.
def select_pivot(arr):
    temp = []
    for _ in range(3):
        temp.append(random.choice(arr))
    temp.sort()
    return temp[1]

def inplace_quick_sort(arr, a, b):
    # a >= b 일경우 return을 해 함수를 빠져나온다.
    if a >= b:
        return
    
    if b - a + 1 >= 3:  # pivot을 3개 뽑고 그 중 중간 값을 사용함으로 3개가 넘을 때만 진행
        pivot = select_pivot(arr[a:b+1])
        # pivot과 같은 값을 찾고 없으면 b를 사용한다.
        pivot_index = b
        for i in range(a, b):
            if arr[i] == pivot:
                pivot_index = i
                break
        # 선택된 pivot을 끝에 둔다, 끝에 둘때 한칸씩 미뤄서 하면 시간복잡도가 증가하므로 swap으로 진행했다.
        arr[pivot_index], arr[b] = arr[b], arr[pivot_index]
    
    # pivot = 맨 끝에 위치
    pivot = arr[b]
    # 왼쪽 인덱스를 가리킴
    l = a
    # 오른쪽 인덱스를 가리킴
    r = b - 1

    while l <= r: # r이 l보다 클때만 반복을 진행한다.
        while l <= r and arr[l] <= pivot: # arr[l]은 pivot 보다 작아야 하므로 작을때 까지 증가시킨다.
            l += 1
        
        while l <= r and arr[r] >= pivot: # arr[r]은 pivot 보다 커야한다.
            r -= 1
        # l < r 인 상태고 현재 arr[l] 과 arr[r] 은 각각 pivot 보다 크고, 작은 값을 가리키고 있다. 따라서 이 둘을 swap한다.
        if l < r:
            arr[l], arr[r] = arr[r], arr[l] # SWAP
        else:
            break
    
    # 정렬이 완료된 상태는 아니다. 하지만 pivot을 기준으로 왼쪽은 작은값, 오른쪽은 큰값이 와 있다.

    # l과 r이 교차했을때 pivot과 l의 위치를 바꾼다.
    arr[l], arr[b] = arr[b], arr[l]
    
    # pivot을 기준으로 왼쪽 오른쪽 재귀 호출을 통해 다시 정렬을 진행핸다.
    inplace_quick_sort(arr, a, l - 1)
    inplace_quick_sort(arr, l + 1, b)
    

def quickSort(arr):
    # 리스트의 길이가 1 이하면 이미 정렬이 끝난 것이다.
    if len(arr) <= 1:
        return arr
    inplace_quick_sort(arr, 0, len(arr) - 1)
    return arr
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''ShellSort를 위한 함수'''
#Knuth의 (3^k-1)/2 general term을 사용했다.
def shellSort(arr):
    n = len(arr)

    h = 1
    # 시작 gap을 설정한다.
    while h < n:
        h = 3 * h + 1
    
    # gap이 1이 될때 까지 감소시키며 반복한다.
    # 마지막에는 일반 정렬과 똑같이 수행한다. 하지만 정렬이 대부분 완료돼있기 때문에 시간 복잡도가 O(N^3/2)일 수 있다.
    while h > 0:
        # 정수형 반환을 위해 // 사용, gap을 감소시킨다.
        h //= 3
        for i in range(h, n):
            temp = arr[i]
            # 현재 위치를 j에 저장한다.
            j = i
            # j가 h보다 커야 그 뒤 비교가 가능하며 arr[j-h] > temp 일 시 arr[j] = arr[j-h], j = j-h를 진행한다.
            while j >= h and arr[j-h] > temp:
                # h만큼 떨어진 값을 j로 이동
                arr[j] = arr[j-h]
                # j index 변환환
                j = j-h
            # 최종 위치 temp를 arr[j]에 초기화한다.
            arr[j] = temp
        
    return arr

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''ParallelSort 위한 함수(Bitonic Sort 사용)'''
# O(log^2n)의 시간복잡도를 갖는다.
# direction이 1이면 오름차순을, 0이면 내림차순 정렬할 수 있도록 정의 했다
def bitonic_sort(arr, l, cnt, direction):
    # 1개 이상 일때만 정렬을 진행한다.
    if cnt > 1:
        mid = cnt // 2
        # bitonic_sort는 오름차순, 내림차순이 한번씩 진행된다. 이를 활용했다.
        bitonic_sort(arr, l, mid, 1)  # 오름차순 정렬
        # 오름차순 이후에는 내림차순으로 진행
        bitonic_sort(arr, l + mid, mid, 0)  # 내림차순 정렬
        bitonic_merge(arr, l, cnt, direction)

def bitonic_merge(arr, l, cnt, direction):
    if cnt > 1:
        # 중간 지점을 계산한다.
        mid = cnt // 2
        # mid 만큼의 비교를 진행한다.
        for i in range(l, l + mid):
            if direction == 1:  # 오름차순 정렬
                if arr[i] > arr[i + mid]:
                    arr[i], arr[i + mid] = arr[i + mid], arr[i]
            else:  #내림차순 정렬
                if arr[i] < arr[i + mid]:
                    arr[i], arr[i + mid] = arr[i + mid], arr[i]

        # 앞부분 merge
        bitonic_merge(arr, l, mid, direction)

        # 뒷부분 merge
        bitonic_merge(arr, l + mid, mid, direction)

def sort(arr):
    bitonic_sort(arr, 0, len(arr), 1)  # 오름차순으로 정렬
    return arr

# bitonic sort는 2의 배수에서만 작동한다. 따라서 이를 맞춰줘야한다.
# 가까운 2의 배수를 찾고 그 배수에 맞춰 배열을 증가시킨다.
def parallelSort(arr):
    n = len(arr)
    temp_n = n

    num = 1
    while num < n:
        num *= 2

    # 이제 num에 맞춰서 배열을 증가시켜야함
    if temp_n != num:
        copied_arr = list(arr.copy())
        for _ in range(num - temp_n):
            copied_arr.append(float('inf'))
        # 정렬을 한 후 추가한 부분을 제외하고 return 한다.
        sort(copied_arr)
        return copied_arr[:temp_n]
    else:
        return sort(arr.copy())

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 실행 시간 측정 함수
def check_performance(sort_algorithm, data, want_to_see):

    # 원본 데이터 유지를 위해 사용한다.
    temp_data = list(data)

    # 시작 시간
    start = time.time()
    
    if want_to_see == 'n':
        # 정렬 알고리즘 실행
        sort_algorithm(temp_data)
    elif want_to_see == 'y':
        print(*sort_algorithm(temp_data))
    
    # 종료 시간
    end = time.time()
    
    # 실행 시간 계산
    runtime = end - start
    
    return runtime
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def main():
    n = int(input('비교할 데이터 셋의 크기를 입력해주세요: '))
    want_to_see = (input('정렬된 데이터를 확인하고 싶으신가요? (y or n): '))

    # data 리스트 생성
    data = []
    for i in range(n):
        # 랜덤 데이터 생성
        data.append(random.randint(1, 1000000))

    # 시간은 소수점 6번째 자리까지 명시
    # format을 사용해서 print
    mergeSort_time = check_performance(mergeSort, data, want_to_see)
    print('데이터 셋이 {0} 일때 MergeSort의 실행 시간은 {1:.6f} 입니다.'.format(n, mergeSort_time))
    quickSort_time = check_performance(quickSort, data, want_to_see)
    print('데이터 셋이 {0} 일때 QuickSort 실행 시간은 {1:.6f} 입니다.'.format(n, quickSort_time))
    shellSort_time = check_performance(shellSort, data, want_to_see)
    print('데이터 셋이 {0} 일때 ShellSort의 실행 시간은 {1:.6f} 입니다.'.format(n, shellSort_time))
    parallelSort_time = check_performance(parallelSort, data, want_to_see)
    print('데이터 셋이 {0} 일때 ParallelSort의 실행 시간은 {1:.6f} 입니다.'.format(n, parallelSort_time))


    # 결과를 막대 그래프로 시각화
    sorting = ['MergeSort', 'QuickSort', 'ShellSort', 'ParallelSort']
    times = [mergeSort_time, quickSort_time, shellSort_time, parallelSort_time]
    
    plt.bar(sorting, times, color=['blue', 'green', 'red', 'black'], width=0.4)
    plt.xlabel('sorting')
    plt.ylabel('runtime(sec)')

    plt.show()

if __name__ == "__main__":
    main()