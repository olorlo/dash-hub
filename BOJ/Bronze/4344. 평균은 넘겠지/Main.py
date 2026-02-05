# 4344번
C = int(input())
for _ in range(C):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    # print(N)
    avg = sum(arr) / N
    cnt = 0
    for i in arr:
        if i > avg:
            cnt += 1

    print(f'{cnt/N*100:.3f}%')