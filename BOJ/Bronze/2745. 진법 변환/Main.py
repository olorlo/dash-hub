# 백준 2745번 진법 변환
N, B = input().split()
change = []
for i in range(26):
    change.append({chr(i+65):10+i})

result = 0 

for i in range(len(N)):
    for j in range(26):
        if N[i] == chr(j+65):
            result += change[j][N[i]] * (int(B) ** (len(N) - 1- i))
print(result)