# 네비게이션
# k번째로 빠르게 갈 수 있는 경로
import heapq

def cal_k():
    queue=[]
    grid[1][0]=0
    heapq.heappush(queue, (0,1))

    while(len(queue) > 0):
        distance, current= heapq.heappop(queue)

        for nextN, nextC in graph[current]:
            cost = nextC + distance
        
            if cost < grid[nextN][k-1]:
                
                grid[nextN][k-1] = cost
                grid[nextN].sort()
                
                heapq.heappush(queue, (cost, nextN))

n, m, k = map(int, input().split())
grid = [[float('inf')] * (k) for _ in range(n + 1)]

graph=[[] for _ in range(n + 1)]

for _ in range(m):
    loc_a, loc_b, time = map(int, input().split())
    graph[loc_a].append((loc_b, time))

start = 1

cal_k()

#k번째 출력
temp = 0
for i in grid:
    if temp == 0:
        temp+=1
        continue
    if i[k-1]==float('inf'):
        print(-1)
    else:
        print(i[k-1])
