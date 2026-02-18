# SWEA 새로운 captcha code

T = int(input())
for tc in range(1, T + 1):
    N , K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    # N개의 길이의 sample
    # K개의 길이의 passcode
    cnt = 0
    a = 0
    for i in range(K):
        for j in range(a, N):
            if passcode[i] == sample[j]:
                a = j
                cnt += 1
                break
    result = 0
    if cnt == K:
        result = 1

    print(f'#{tc} {result}')