def convert_to_number(text):
  '''
  Mindent számmá alakít! A boolean értéket is.
  '''
  try:
    szam = int(text)
    return True
  except ValueError:
    return False
  # except:  # így minden hibát elkap
  #   return False


def print_hello(count: int):
  try:
    for i in range(count):
      print(f"{i+1}. Helló!")
  except:
    print("Valami hiba történt!")


szam = input("Adj meg egy számot")
if convert_to_number(szam) and int(szam) > 0:  # ide azért írhattam, hogy int(szam), mert ha az első feltétel nem teljesül, akkor a masodik ki sem értékelődik, azza biztos lehetek benne, hogy a szam változó szám.
  print_hello(int(szam))
else:
  print("Számot adj meg, amely nagyobb nullánál!")
