# swea Tree 사칙연산

T = 10

def postorder(node):
    # 숫자노드면 그대로 반환
    if tree[node][1] == 0 and tree[node][2] == 0:
        return float(tree[node][0])
    
    left = postorder(tree[node][1])
    right = postorder(tree[node][2])
    operator = tree[node][0]

    if operator =='+':
        result = left + right
    elif operator =='-':
        result = left - right
    elif operator == '*':
        result = left * right
    elif operator == '/':
        result = left / right

    return result
    
for tc in range(1, T+1):
    N = int(input())

    tree = [0]*(N+1)

    for _ in range(N):
        arr = input().split()
        node = int(arr[0])
        
        # 숫자 노드
        if arr[1].isdigit():
            tree[node] = [arr[1], 0, 0]

        # 연산자 노드
        else:
            tree[node] = [arr[1], int(arr[2]), int(arr[3])]

    result = postorder(1)

    print(f'#{tc} {int(result)}')