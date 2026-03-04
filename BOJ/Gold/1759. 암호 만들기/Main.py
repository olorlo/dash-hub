import sys
# sys.stdin = open("python/input.txt", 'r')
input = sys.stdin.readline

# 백준 1759번 암호 만들기
L, C = map(int, input().split())
arr = input().split()
arr.sort()

def dfs(node, stack):
    global cnt_c, cnt_v
    visited[node] = 1
    stack.append(arr[node])

    if arr[node] in ['a', 'e', 'i', 'o', 'u']:
        cnt_v += 1
    else:
        cnt_c += 1
    
    if len(stack) == L:
        if cnt_v >= 1 and cnt_c >=2 :
            print(''.join(stack))
            return 

    # 알파벳 순서로 만들기위해서 node부터 시작
    for next in range(node+1, C):
        if visited[next]:
            continue
        
        dfs(next, stack)
        # dfs를 돌고 나온 후 stack pop해주고 사전 순으로 다른 단어 만들기
        stack.pop()
        
        # stackpop해주었으니까 pop해준 단어 cnt -1 
        if arr[next] in ['a', 'e', 'i', 'o', 'u']:
            cnt_v -= 1
        else:
            cnt_c -= 1
        
        visited[next] = 0

result = 0

visited = [0] * C

for i in range(C):
    cnt_v = 0
    cnt_c = 0
    dfs(i, [])