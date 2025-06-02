import heapq
import sys
#input= lambda: sys.stdin.readline().strip('\n')
#최대값으로 초기화
INF= sys.maxsize

n,m,k= map(int, input().split())

distance=[[INF] * (k)  for _ in range(n+1)]

#간선 입력받기
graph=[[] for _ in range(n+1)]

for _ in range(m):
  a,b,c= map(int, input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q=[]
  distance[start][0]=0
  heapq.heappush(q, (0,start))

  while(q):
    dist, now= heapq.heappop(q)

    for next_node, next_cost in graph[now]:
      cost= next_cost+dist
	  
      #상위 k번째 안에 속하는가?
      if cost<distance[next_node][-1]:
      		
            #속하면 꼴등이랑 switch ->정렬
            distance[next_node][-1]=cost
            distance[next_node].sort()
            
            heapq.heappush(q, (cost, next_node))

dijkstra(1)

#k번째만 출력해주기
for i in distance[1:]:
  if i[k-1]>=INF:
    print(-1)
  else:
    print(i[k-1])