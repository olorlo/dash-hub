
from collections import deque

# SWEA 5102 노드의 거리

T = int(input())

def bfs(node):
    dq = deque([node])
    visited[node] = 0

    while dq:
        now_node = dq.popleft()
    
        if now_node == G:
            return visited[now_node]
        
        for next in graph[now_node]:
            if visited[next] != -1:
                continue
            visited[next] = visited[now_node] + 1
            dq.append(next)

    return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph =[[] for _ in range(V+1)]
    visited = [-1] * (V+1)
    cnt = 0

    for _ in range(E):
        first, end = map(int, input().split())
        graph[first].append(end)
        graph[end].append(first)

    S, G = map(int, input().split())

    result = bfs(S)

    print(f'#{tc} {result}')