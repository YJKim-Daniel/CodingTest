# 입력 받기
n_dim = int(input())
l_direction = input().split()

# 방향에 따른 벡터 정의
dir = {'L':(0, -1), 'R':(0, 1), 'U':(-1, 0), 'D':(1, 0)}

# 시작점 정의
x, y = 0, 0

# 이동 loop
for k in l_direction:
  
  # 좌표 업데이트
  # max를 통한 boundary 제한
  x = max(0, x + dir[k][0])
  y = max(0, y + dir[k][1])

print(x+1, y+1)

# 5
# R R R U D D