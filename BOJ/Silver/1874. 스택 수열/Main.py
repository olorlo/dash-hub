# 백준 1874번 스택 수열
n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
result = []
idx = 0
i = 1
while True:

    if result == arr:
        break
    
    while stack:
        if arr[idx] == stack[-1]:
            result.append(stack.pop())
            print('-')
            idx += 1
        else: 
            break

    if i >= n + 1:
        break
    stack.append(i)
    print('+')
    i += 1
