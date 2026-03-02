
from collections import deque

# swea 21829 bfs기초-방문순서출력하기
T = int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(node):
    dq = deque([node])
    visited[node] = 1

    while dq:
        now = dq.popleft()
        print(now, end = ' ')
        for next in graph[now]:
            if visited[next]:
                continue
            visited[next] = 1
            dq.append(next)      

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    graph = [[] for _ in range(N)]
    visited = [0] * N

    # 인접 리스트로 만들기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                graph[i].append(j)
    
    # 그래프 정렬
    for i in range(N):
        graph[i].sort()

    print(f'#{tc}', end= ' ')
    bfs(0)
    print()