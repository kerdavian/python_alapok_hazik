
import math


def convert_to_number(text):
  '''
  Mindent számmá alakít! A boolean értéket is.
  '''
  try:
    szam = int(text)
    return True
  except ValueError:
    return False


def kor_kerulet(sugar):
  return 2*float(sugar)*math.pi


def kor_teruelt(sugar):
  return float(sugar)*float(sugar)*math.pi


szam = input("Add meg kör sugarát!")

if convert_to_number(szam) and int(szam) > 0:
  print(f"A kör kerülete {round(kor_kerulet(szam), 2)}\nA kör területe {round(kor_teruelt(szam), 2)}")
else:
  print("Számot adj meg, amely nagyobb nullánál!")

