# 백준 10813번
# 공 바꾸기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

box = {}
for i in range(1,N+1):
    box[i]=i

for m in range(M):
    box[arr[m][0]],box[arr[m][1]] = box[arr[m][1]],box[arr[m][0]]

print(*box.values())