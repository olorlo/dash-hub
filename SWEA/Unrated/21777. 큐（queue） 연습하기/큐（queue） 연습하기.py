
from collections import deque

# SWEA 큐 연습하기
N = int(input())
dq = deque()
for _ in range(N):
    command = input().split()
    if command[0] == 'enqueue':
        dq.append(command[1])
    elif command[0] == 'dequeue':
        print(dq.popleft())
        
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'isEmpty':
        if len(dq) == 0:
            print('1')
        else:
            print('-1')
    elif command[0] == 'front':
        if len(dq) == 0:
            print('-1')
        else:
            print(dq[0])
    elif command[0] == 'rear':
        if len(dq) == 0:
            print('-1')
        else:
            print(dq[-1])
    
