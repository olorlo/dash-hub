# SWEA 1231 중위순회
T = 10

def inorder(node):
    # leaf 일 때
    if node == 0:
        return
    
    # 왼쪽 노드로 이동
    inorder(tree[node][1])

    print(tree[node][0], end='')
    
    # 오른쪽 노드로 이동
    inorder(tree[node][2])

for tc in range(1, T+1):

    # 정점의 총 수 
    N = int(input())
    
    tree = [0] * (N+1)

    for _ in range(N):
        info = input().split()
        node = int(info[0])
        char = info[1]

        if len(info) == 4:
            left = int(info[2])
            right = int(info[3])
        elif len(info) == 3:
            left = int(info[2])
            right = 0
        else:
            left = right = 0
        
        tree[node] = (char, left, right)
    
    print(f'#{tc}', end= ' ')
    inorder(1)
    print()