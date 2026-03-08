import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

# 5014번 스타트링크
def bfs(cur):
    dq = deque([cur])
    
    while dq:
        now = dq.popleft()

        if now == G:
            return visited[G]
        
        # 현재 위치에서 갈 수 있는 경우의 수
        for next in (now+U, now-D):
            if next < 0 or next >F:
                continue
            if visited[next]:
                continue

            visited[next] = visited[now] + 1
            # cnt += 1
            dq.append(next)
            
    return 'use the stairs'

F, S, G, U, D = map(int, input().split())
visited = [0]*(F+1)
result = bfs(S)
print(result)