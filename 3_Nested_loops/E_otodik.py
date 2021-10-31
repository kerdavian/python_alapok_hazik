my_list = [[4, 5], [7, 4], [2, 5], [9, 4]]

for index, lista in enumerate(my_list):
  my_list[index].append(my_list[index][0] + my_list[index][1])

print(my_list)