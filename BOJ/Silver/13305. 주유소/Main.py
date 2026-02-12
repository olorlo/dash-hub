# 백준 13305번 주유소

N = int(input())
road_len = list(map(int, input().split()))
station = list(map(int, input().split()))
min_fee =10000
fee = 0
i = 0

# while True: (틀린 코드)
    # if station[i] >= station[i+1]:
    #     fee += station[i] * road_len[i]
    #     i+=2
    # else:
    #     fee += station[i] * (road_len[i]+road_len[i+1]) 
    #     i += 2
    # if i >= len(road_len):
    #     break

for i in range(len(road_len)):
    if station[i] <= min_fee:
        min_fee = station[i] 
    fee += min_fee * road_len[i]

print(fee)