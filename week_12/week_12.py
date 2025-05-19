def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx < ry:
        root[rx] = ry
    else:
        root[rx] = ry

n = int(input()) # 도시의 수
m = int(input()) # 도로의 수

root = {i: i for i in range(1, n+1)}
edges = []

for i in range(m):
    # 도로 공사 비용
    # a도시와 b도시 사이의 고사 비용 C
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
# a에서 b로 가는데 c 의 비용을 그래프로 표현

# 크루스칼이라 최소 비용으로 sorting
edges = sorted(edges)
result = 0
for c, a, b in edges:
    if find(a) == find(b):
        continue
    
    union(a, b)
    result += c

print(result)