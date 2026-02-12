# 백준 12891번 DNA 비밀번호
S, P = map(int, input().split())
DNA = list(input()) 
condition = list(map(int, input().split())) 
result = 0
password = DNA[:P] 

cnt = [0] * 4
for j in password:
    if j == 'A':
        cnt[0] += 1
    elif j == 'C':
        cnt[1] += 1
    elif j == 'G':
        cnt[2] += 1
    elif j == 'T':
        cnt[3] += 1
    if cnt[0] >= condition[0] and cnt[1] >= condition[1] \
        and cnt[2] >=condition[2] and cnt[3] >= condition[3]:
        result += 1

for i in range(S-P):
    cnt = [0] * 4
    password.remove(DNA[i])
    password.append(DNA[i + P])
    for j in password:
        if j == 'A':
            cnt[0] += 1
        elif j == 'C':
            cnt[1] += 1
        elif j == 'G':
            cnt[2] += 1
        elif j == 'T':
            cnt[3] += 1
        
        
        if cnt[0] >= condition[0] and cnt[1] >= condition[1] \
            and cnt[2] >=condition[2] and cnt[3] >= condition[3]:
            result += 1
print(result)
