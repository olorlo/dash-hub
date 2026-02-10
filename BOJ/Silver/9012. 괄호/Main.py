# 백준 9012번
T = int(input())
for tc in range(T):
    arr = input()
    stack = []
    result = 'YES'
    for i in arr:
        if i =='(':
            stack.append(i)
        else: # 닫힌 괄호 일 경우 
            if not stack:
                result = 'NO'
                break
            stack.pop()
        
    if stack:
        result = 'NO'

    print(result)