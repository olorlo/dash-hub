# swea 21684. 미로

T = int(input())

# 델타로 주변 탐색
dy = [-1, 1, 0, 0] # 상 하 좌 우 
dx = [0, 0, -1, 1]

def escape(row, col):
    # 종료 조건(가치지기?): 3을 만났는지 확인
    # 주변에 3 존재 -> return 하고 1을 출력
    if maze[row][col] == '3':
        return 1

    # for문: 주변에 0이 있는지 확인
    # 0 이 있으면 해당 위치로 이동
    for k in range(4):
        ny = row + dy[k]
        nx = col + dx[k]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if maze[ny][nx] =='0' or maze[ny][nx] =='3':
            if visited[ny][nx] == 1:
                continue
            visited[ny][nx] = 1
            if escape(ny, nx):
                return 1
    
    return 0

for tc in range(1, T + 1):
    
    # 미로의 크기
    N = int(input())

    #(0은 통로, 1은 벽, 2는 출발, 3은 도착이다.)
    maze = [input() for _ in range(N)]

    visited = [[0]*N for _ in range(N)]
    
    print(f'#{tc}', end=' ')

    # 반복문으로 maze 속 2와 3을 찾은 뒤 해당 위치 인덱스를 저장
    # escape 함수로 들어가서 2에서 부터 시작
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                print(escape(i,j))