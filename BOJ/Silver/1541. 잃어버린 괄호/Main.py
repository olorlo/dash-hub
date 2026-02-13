
# 백준 1541번 잃어버린 괄호

# # 수식을 기준으로 나누는 방법
# import re
# arr = re.split(r'([+-])', input())

s = input().split('-')
result = sum(map(int, s[0].split('+')))
for i in s[1:]:
    result -= sum(map(int, i.split('+')))

print(result)