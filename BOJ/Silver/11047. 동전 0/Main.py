# 백준 11047번
# 동전 0

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
a =0
cnt = 0

while K > 0:
    # arr 값 중 K보다 작지만 그중 최대 값 a
    for i in arr:
        if i < K:
            a=i
    cnt += K // a
    K = K % a

print(cnt)