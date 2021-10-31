from typing import List


def what_typeof(in_list: List) -> List:
  type_list = []
  type_dict = {int: "integer", str: "string", bool: "boolean"}

  for elem in in_list:
    type_list.append(type_dict[type(elem)])

  return type_list


x = ['', 4, True]
list_of_type = what_typeof(x)
print(list_of_type)