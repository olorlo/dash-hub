# 백준 2839번
N = int(input())
cnt = 0
min_cnt = 1000
result = -1
while N>=3:
    if N % 5 ==0:
        cnt += 1
        N -= 5
    else:
        cnt += 1
        N -= 3
    if N ==0:
        break
    elif 0 <N < 3 or  N < 0:
        result = -1
        break
        
if N != 0:
    print(result)
else:
    print(cnt)