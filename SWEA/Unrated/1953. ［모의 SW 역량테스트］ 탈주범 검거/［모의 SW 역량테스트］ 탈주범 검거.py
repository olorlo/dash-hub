from collections import deque

# swea 탈주범 검거
T = int(input())

# 구조물에 따른 방향 설정
# 상하좌우 = 0123
structure = {
    1: [0,1,2,3],
    2: [0,1],
    3: [2,3],
    4: [0,3],
    5: [1,3],
    6: [1,2],
    7: [0,2]
}

# 하상우좌
opposite = [1, 0, 3, 2]

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    dq = deque()
    dq.append((R, C, 1))
    visited[R][C] = 1
    cnt = 1
    
    while dq:
        now_y, now_x, time = dq.popleft()
        
        if time == L:
            continue
        
        now = arr[now_y][now_x]
        for k in structure[now]:
            ny = now_y + dy[k]
            nx = now_x + dx[k]
            
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            
            # 이동한 곳이 나를 받을 수 있는 곳인가?
            # 1. 길이 있는지 + 방문 했는지
            # 2. 그 길이 나랑 이어져있는지
            if arr[ny][nx] != 0 and not visited[ny][nx]:
                if opposite[k] in structure[arr[ny][nx]]:
                    visited[ny][nx] = 1
                    cnt += 1
                    dq.append((ny, nx, time +1))
                    
    return cnt 

for tc in range(1, T+1):
    # 세로크기 N, 가로 크기 M, 맨홀 뚜껑 위치 R, C, 탈출 후 소요 시간 L
    N, M, R, C, L = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    
    result = bfs()
    
    print(f'#{tc} {result}')