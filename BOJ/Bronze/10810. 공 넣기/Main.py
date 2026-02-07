# 백준 20810번
# 공 넣기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
print(arr)

box = {}
for i in range(1,N+1):
    if box.get(i,None) == None:
        box[i]=0

# arr[M][0,1,2]
for m in range(M):
    print('arr 행: ',m)
    # for i in range(m+1):
    for j in range(arr[m][0],arr[m][1]+1):
        print('j: ',j)

        if box.get(j,None) == None:
            box[j]=0

        box[j]=arr[m][2]
        print('box: ',box)


print(*list(box.values()))