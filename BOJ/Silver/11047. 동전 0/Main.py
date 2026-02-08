# 백준 11047번
# 동전 0

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
cnt = 0
arr = list(reversed(arr))

for i in arr:
    cnt += K // i
    K %= i

print(cnt)