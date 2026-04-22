
from collections import deque

# swea 벽돌 깨기
T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(cnt, game):
    global result 
    # 매번 다른 게임판 써야함
    
    # 종료조건: 구슬 모두 다 썼을 때 종료
    if cnt == N:
        cnt_brick = 0
        for i in range(H):
            for j in range(W):
                if game[i][j] > 0:
                    cnt_brick += 1
                    
        result = min(result, cnt_brick)
        return
     
    # 무슨 열에 구슬 치기할 지 결정
    for x in range(W):
        if all(game[y][x] == 0 for y in range(H)):
            continue
        new_game = [row[:] for row in game]
        
        # 구슬 치기함
        bfs(x, new_game)
        
        # 중력 작용
        gravity(new_game)
        
        # 다시 열 결정
        dfs(cnt+1, new_game)    


# 해당 위치 벽돌 다 깨기
def bfs(x, game):
    dq = deque()

    # 제일 위에 벽돌 넣기
    for y in range(H):
        if game[y][x]:
            dq.append((y, x, game[y][x]))
            game[y][x] = 0
            break
    else:
        return
    
    while dq:
        # 맨 위에 것들 중 하나 뽑음
        now_y, now_x, weight = dq.popleft()
        
        # 벽돌에 적힌 수만큼 제거해야함
        
        # 현재 벽돌 제거
        game[now_y][now_x] = 0
    
        for k in range(4):         
            # 벽돌에 적힌 수만큼 제거하기 위해 큐에 넣기
            for dist in range(1, weight):
                ny = now_y + dy[k]*dist
                nx = now_x + dx[k]*dist
                
                if ny < 0 or ny >= H or nx < 0 or nx >= W:
                    break
                
                if game[ny][nx]:
                    dq.append((ny, nx, game[ny][nx]))
                    game[ny][nx] = 0

            
# 중력 처리
def gravity(game):
    for x in range(W):
        stack = []
        for y in range(H):
            # 값이 있다면 stack에 넣음 
            if game[y][x]:
                stack.append(game[y][x])
        
        for y in range(H-1, -1, -1):
            if stack:
                game[y][x] = stack.pop()
            else:
                game[y][x] = 0
            

for tc in range(1, T+1):
    # N: N개의 구슬, WxH 배열
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    
    result = float('inf')
    dfs(0, arr)
    
    if result == float('inf'):
        result = 0
    
    print(f'#{tc} {result}')