import sys
# sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")

from collections import deque

# 백준 1987번 알파벳

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs():
    global max_value
    # 재귀로 하니까 시간 초과나서 스택 dfs로 수정
    stack.append((0, 0, 1 << start, 1))

    while stack:
        y, x, mask, cnt = stack.pop()
        max_value = max(max_value, cnt)

        if max_value == 26:
            break

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < R and 0 <= nx < C:
    
                # 시간 초과 코드
                # if arr[ny][nx] in stack:
                #     continue
                # -> bitmask로 수정
                # 비트마스크란? 리스트 말고 하나의 문자로 방문했는지 안했는지 체크하는 것

                alpha = ord(arr[ny][nx]) - 65

                # 이미 방문한 곳이라면 지나감
                # alpha 자리에 스위치가 켜져있고, mask 그렇다면 같은 곳을 방문한 것 -> 그냥 지나간다
                if mask & (1 << alpha):
                    continue

                stack.append((ny, nx, mask | (1 << alpha), cnt + 1))
    

max_value = 0
start = ord(arr[0][0]) - 65
stack = []

dfs()

print(max_value)