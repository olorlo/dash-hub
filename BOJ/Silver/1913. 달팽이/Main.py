# 백준 1913번
# 달팽이
N =int(input())

find = int(input())
# 좌표 찾을 때 좌표 저장할 변수
x_index = 0
y_index = 0

arr = [[0]*N for _ in range(N)]

current= N*N #현재 값
direction = 0 # 현재 바라보는 방향

# 현재 좌표
x, y = 0 ,0


# 하 우 상 좌
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while 0<current <= N*N:
    arr[y][x] = current
    if arr[y][x] == find:
        y_index = y + 1
        x_index = x + 1
    ny = y + dy[direction]
    nx = x + dx[direction]

    # 뱡향 전환(다음 좌표가 범위 밖 or 이미 데이터 존재)
    if ny < 0 or ny >=N or nx <0 or nx >=N or arr[ny][nx]:
        direction = (direction + 1) % 4

    current -= 1
    y = y + dy[direction]
    x = x + dx[direction]


for i in arr:
    print(*i)

print(y_index, x_index)