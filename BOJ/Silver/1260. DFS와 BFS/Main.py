import sys

from collections import deque

def dfs(v):
    print(v, end=' ')
    # dfs 는 재귀 사용
    visited2[v] = 1
    # 종료 조건
    if v == N+1:
        # print(lst)
        return 1
    # 종료 조건이 아니라면 
    for next in graph[v]:
        if visited2[next] == 0:
            if dfs(next):
                return
    return
        # lst.append(graph[start][i])
        # dfs(start+1, lst)
        # if dfs(start+1, lst):
        #     return lst
            
def bfs(start):
    dq= deque([start])
    visited1 = [0] * (N+1)
    visited1[start] = 1
    print(start, end = ' ')
    while dq:
        # dq에서 꺼낸다
        now = dq.popleft()
        # 꺼낸 값이 graph와 연결된 값 있는지 확인
        for i in graph[now]:
            if visited1[i] == 1:
                continue
            # 값이 이미 방문된 값이 아니라면 그 곳을 방문 후 큐에 넣음
            visited1[i] = 1
            print(i, end =' ')
            dq.append(i)

# 입력
N, M, V = map(int, input().split())
vertices = [list(map(int, input().split())) for _ in range(M)]

# 양방향 그래프 만들기
graph = [[] for _ in range(N+1)]
for a, b in vertices:
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()
# print(graph)

visited2 = [0] * (N + 1)

dfs(V)
print()
bfs(V)