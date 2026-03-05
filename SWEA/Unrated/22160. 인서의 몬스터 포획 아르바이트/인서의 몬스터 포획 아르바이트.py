# import sys
from collections import deque
# sys.stdin = open("python/input.txt", 'r')
# input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# bfs로 (sy, sx) 위치에서 모든 칸까지 최단거리 계산
def bfs_distance(sy, sx):

    # 방문 초기화
    # visited: (y, x)에서 마을의 모든 칸까지 최단 거리를 2차원 배열로 만듦
    visited = [[-1]*N for _ in range(N)]
    dq = deque()
    dq.append((sy, sx))

    # (sy, sx) 방문 처리
    visited[sy][sx] = 0

    while dq:
        # 현재 위치
        y, x = dq.popleft()

        # 상하좌우 검사
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            # 방문하지 않았고, 범위 초과했을 때 거리 갱신 후 해당 좌표 덱에 넣기
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                dq.append((ny, nx))

    return visited

# 총 시간 계산
def dfs(pos_y, pos_x, caught, delivered, time):
    global min_time
    if len(delivered) == total_monster:
        min_time = min(min_time, time)
        return

    # 남은 몬스터 잡기
    for my, mx, mnum in monster_pos:
        if mnum not in caught:
            # 잡은 몬스터 추가
            caught.append(mnum)
            dfs(my, mx, caught, delivered, time + dist[(pos_y, pos_x)][my][mx])
            # 돌아와서 상태 되돌림
            caught.pop()

    # 잡은 몬스터 전달
    for py, px, pnum in person_pos:
        if pnum in caught and pnum not in delivered:
            # 전달 완료 
            delivered.append(pnum)
            dfs(py, px, caught, delivered, time + dist[(pos_y, pos_x)][py][px])
            # 상태 되돌림
            delivered.pop()

# 테스트케이스
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    monster_pos = []
    person_pos = []
    total_monster = 0

    for i in range(N):
        for j in range(N):
            # 몬스터 위치 저장
            if arr[i][j] > 0:
                monster_pos.append((i, j, arr[i][j]))
                total_monster += 1
            # 의뢰자 위치 저장
            elif arr[i][j] < 0:
                person_pos.append((i, j, -arr[i][j]))

    # 위치 간 최단 거리 미리 계산
    positions = [(0,0)] + [(y,x) for y,x,_ in monster_pos + person_pos]
    dist = {}
    # 중요 위치까지 거리
    for y, x in positions:
        # dfs_distance: 
        dist[y,x] = bfs_distance(y, x)
    
    min_time = 100000000
    dfs(0, 0, [], [], 0)

    print(f"#{tc} {min_time}")