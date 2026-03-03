# swea 그래프마스터 - 바이러스는 무서워
from collections import deque

T = int(input())

def bfs(node):
    global cnt
    dq = deque([node])
    visited[node] = 1
    while dq:
        now = dq.popleft()
        for next in graph[now]:
            if visited[next]:
                continue
            visited[next] = 1
            cnt += 1
            dq.append(next)
    print(cnt)


for tc in range(1, T+1):
    cnt = 0
    n = int(input())
    pair = int(input())

    # 양방향 그래프 만들기
    graph = [[] for _ in range(n+1)]
    for _ in range(pair):
        c1, c2 = map(int, input().split())
        graph[c1].append(c2)
        graph[c2].append(c1)

    visited = [0] * (n+1)

    print(f'#{tc} ', end = '')

    bfs(1)