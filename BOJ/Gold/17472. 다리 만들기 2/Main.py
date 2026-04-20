import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

from collections import deque

# 백준 17472 다리 만들기 2

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# 1. bfs로 섬 번호 붙이기
number = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not visited[i][j]:
            number += 1
            arr[i][j] = number
            
            q = deque([(i, j)])
            visited[i][j] = 1
            
            while q:
                now_i, now_j = q.popleft()
                
                for k in range(4):
                    ni = now_i + dy[k]
                    nj = now_j + dx[k]
                    
                    if ni < 0 or ni >= N or nj < 0 or nj >= M:
                        continue
                    
                    if visited[ni][nj]:
                        continue
                    
                    if arr[ni][nj]:
                        arr[ni][nj] = number
                        visited[ni][nj] = 1
                        q.append((ni, nj))

# for i in range(len(arr)):
#     print(arr[i])

# 2. 직선 다리 길이 계산
graph = [[] for _ in range(number+1)]
def cal(n):
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == n:
                
                # 경계 체크
                is_edge = False
                for d in range(4):
                    di = i + dy[d]
                    dj = j + dx[d] 
                    if di < 0 or di >= N or dj < 0 or dj >= M:
                        continue
                    if arr[di][dj] == 0:
                        is_edge = True
                        
                if is_edge:
                    for k in range(4):
                        bridge = 0
                        ni = i
                        nj = j
                        
                        while True:
                            ni += dy[k]
                            nj += dx[k]
                            
                            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                                break
                            
                            # 다리 건설: 0을 만남 
                            if arr[ni][nj] == 0:
                                bridge += 1
                        
                            # 바다 건너 자기자신 만남
                            if arr[ni][nj] == n:
                                break
                                    
                            # 다리 확정: 0이 아닌 arr를 만남                        
                            elif arr[ni][nj] and arr[ni][nj] != n:
                                if bridge >= 2:
                                    graph[n].append((n, arr[ni][nj], bridge))
                                break
               
for i in range(1, number+1):
    cal(i)

# 간선 정리
edges = []
for i in range(1, number+1):
    for (a, b, cost) in graph[i]:
        edges.append((cost, a, b))

edges.sort()

# 3. MST(union find)로 최단 거리 계산
parent = [i for i in range(number+1)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rep_a = find(a)
    rep_b = find(b)
    
    if rep_a != rep_b:
        parent[rep_b] = rep_a

result = 0
cnt = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += cost
        cnt += 1

if cnt == number -1:
    print(result)
else:
    print(-1)