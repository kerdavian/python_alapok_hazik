from typing import List

def sort_a_list(in_list: List):
  sorted_list = sorted(in_list)

  first_part = int(round(len(sorted_list)/2, 0))
  
  print(first_part)
  print("\t1. csoport")
  for i in range(first_part):
    print(sorted_list[i])
  
  print("\t2. csoport")
  for i in range(first_part, len(sorted_list)):
    print(sorted_list[i])




names = ['Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter', 'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs', 'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás' ]

sort_a_list(names)

