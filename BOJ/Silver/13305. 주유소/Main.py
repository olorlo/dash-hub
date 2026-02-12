# 백준 13305번 주유소

N = int(input())
road_len = list(map(int, input().split()))
station = list(map(int, input().split()))
fee = 0
i = 0
while True:
    if station[i] >= station[i+1]:
        fee += station[i] * road_len[i]
        i+=1
    else:
        fee += station[i] * (road_len[i]+road_len[i+1]) 
        i += 2
    if i >= len(road_len):
        break
    
print(fee)