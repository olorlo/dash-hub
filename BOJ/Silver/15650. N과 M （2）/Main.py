# 백준 15650번 N, M (2)

def bt(n,path):

    if len(path) == M:
        print(*path)
        return 
    for i in range(n, N+1):
        path.append(i)
        bt(i+1,path)
        path.pop()


N, M = map(int, input().split())

visited = [0] * (N+1)
bt(1,[])
