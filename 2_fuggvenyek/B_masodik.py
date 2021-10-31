from typing import List


def count_of_name(in_list: List, name: str) -> int:
  return in_list.count(name)


names = [
    'Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István', 'László',
    'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista'
]

print(count_of_name(names, "Pista"))