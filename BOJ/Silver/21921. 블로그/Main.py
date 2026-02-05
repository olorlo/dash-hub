N, X = map(int, input().split())
arr = list(map(int, input().split()))
window = sum(arr[:X])
max_sum = window
cnt = []
cnt1 = 0

for i in range(len(arr)-X):
    window = window - arr[i] + arr[i+X]
    if window >= max_sum:
        max_sum = window
        cnt.append(max_sum)

for j in range(len(cnt)):
    if max_sum == cnt[j]:
        cnt1 += 1

if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(cnt1)