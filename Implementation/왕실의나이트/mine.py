loc = input()

# 0, 0으로 영점 조정
x = ord(loc[0]) - ord('a')
y = int(loc[1]) - 1

# 이동 가능한 방향 벡터 생성
# vector = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (1,-2), (-1,2), (1,2)]
get_combi = [(tmp_1, tmp_2) for tmp_1 in (-2, 2) for tmp_2 in (-1, 1)]
get_reversed_combi = [(y,x) for x, y in get_combi]
vector = get_combi + get_reversed_combi

# print(vector)

n_case = 0
for dx, dy in vector:
  
  # 체스판의 끝 경계 조건을 잊으면 안됨
  if 0 <= x + dx < 8 and 0 <= y + dy < 8:
    n_case += 1

print(n_case)
