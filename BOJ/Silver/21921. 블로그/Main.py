

N, X = map(int, input().split())
arr = list(map(int, input().split()))
window = sum(arr[:X])
max_sum = window
cnt = 1

for i in range(N - X):
    window = window - arr[i] + arr[i+X]
    if window > max_sum:
        max_sum = window
        cnt =1
    elif window == max_sum:
        cnt+=1
        
if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(cnt)

