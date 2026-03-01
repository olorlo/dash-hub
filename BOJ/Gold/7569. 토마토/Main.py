import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

from collections import deque

# 백준 7569번 토마토
M, N, H = map(int, input().split())

dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 토마토 박스 입력
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

def bfs(z, y, x):
    # 일단 넣음
    dq = deque([(z, y, x)])

    # 넣은 것들 중에서 아래위상하좌우 체크
    while dq:
        now_z, now_y, now_x = dq.popleft()
        for k in range(6):
            nz = now_z + dz[k]
            ny = now_y + dy[k]
            nx = now_x + dx[k]

            if nz < 0 or nz >= H or\
                ny < 0 or ny >= N or\
                nx < 0 or nx >= M:
                continue
            
            # 토마토 박스가 비었음 -> pass
            if tomatoes[nz][ny][nx] == -1:
                continue

            # 현재: 이미 익은 토마토 -> pass 
            if tomatoes[now_z][now_y][now_x]:
                continue
            
            # 현재 안익은 토마토인데 아래위상하좌우 중 익은 토마토 존재 
            # -> 현재 토마토도 익음
            if tomatoes[nz][ny][nx] == 1:
                tomatoes[now_z][now_y][now_x] = 1
            
            # 현재 안 익은 토마토면 아래위상하좌우 모두 덱에 넣음
            dq.append([nz, ny, nx])

cnt = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            # 익은 토마토일 떄 
            if not tomatoes[h][n][m]:
                bfs(h, n, m)
                # 현재 토마토 지점에서 bfs 돌았는데 토마토가 익었다 -> 날짜 세기
                if tomatoes[h][n][m]:
                    cnt += 1

if cnt == 1:
    result = 0
else:
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatoes[h][n][m] == 0:
                    result = -1
                    break
                else:
                    result = cnt
            if result == -1:
                break
        if result == -1:
            break
print(result)