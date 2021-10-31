matrix = [[1, 1, 1, 2, 1], [2, 3, 2, 2, 2], [3, 3, 2, 3, 3], [4, 4, 4, 3, 4]]

summ = 0
# 1. megoldás
for lista in matrix:
  for elem in lista:
    summ = summ + elem

# 2. megoldás
# for lista in matrix:
#   summ = summ + sum(lista)

print(summ)