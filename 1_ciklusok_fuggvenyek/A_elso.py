nums = [3, 4, 9, 6, 2]
yes = "osztható kettővel"
no = "nem osztható kettővel"

for num in nums:
  print(f"{num}: {yes}" if num % 2 == 0 else f"{num}: {no}")
