import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 백준 17281 야구

# 이닝 수
inning = int(input())

# 각 선수가 각 이닝에서 얻는 결과
# 안타: 1, 2루타: 2, 3루타: 3, 홈런: 4, 아웃: 0
arr = [list(map(int, input().split())) for _ in range(inning)]

visited = [0] * 9
max_score = 0

# 타순 결정
def decide(team):
    global max_score
    if len(team) == 9:

        score = simulation(team)
        max_score = max(max_score, score)
        return
    
    for i in range(9):
        if visited[i]:
            continue
        
        # 4번 타자가 무조건 0번 선수
        if len(team) == 3:
            if visited[0]:
                continue
            visited[0] = 1

            # 0번 선수가 방문되지 않았다면 팀에 추가한다.
            team.append(0)
            decide(team)
            team.pop()
            visited[0] = 0

            # 4번 타자 자리에서는 일반 경우를 실행하지 않기위해서 continue
            continue

        # 일반 경우: 4번 타자 자리가 아닐 때
        visited[i] = 1
        team.append(i)
        decide(team)
        team.pop()
        visited[i] = 0

def simulation(team):
    score = 0
    batter_idx = 0 # 현재 타자 위치

    for i in range(inning):
        out = 0
        b1, b2, b3 = 0, 0, 0 # 1루, 2루, 3루

        while out < 3:
            # 현재 플레이어: 현재 타자위치
            player = team[batter_idx]
            result = arr[i][player]

            # 아웃
            if result == 0:
                out += 1
            
            # 안타
            elif result == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2

            # 2루타
            elif result == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1

            # 3루타
            elif result == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1

            # 홈런
            elif result == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0

            batter_idx = (batter_idx+1)%9
    return score

decide([])
print(max_score)