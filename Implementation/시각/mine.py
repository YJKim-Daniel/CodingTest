t = int(input())

cnt = 0
for h in range(t+1):

  if h % 10 == 3:
    cnt += 3600
    continue

  for m in range(60):

    if (m // 10 == 3) or (m % 10 == 3):
      cnt += 60
      continue

    for s in range(60):

      if (s // 10 == 3) or (s % 10 == 3):
        cnt += 1
        continue

print(cnt)