import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 백준 2493번 탑
N = int(input())
stack = list(map(int, input().split()))

# stack = []
result = []
while True:
    a= stack.pop()
    if not stack:
        result.append(0)
        break
    if a > max(stack):
        result.append(0)
    else:
        for i in range(len(stack)-1,-1,-1):
            if a < stack[i]:
                result.append(i+1)
                break

print(*list(reversed(result)))


