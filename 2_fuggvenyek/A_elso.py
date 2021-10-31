from typing import List


def pro_division(start: int, finish: int, divisible: int,
                 not_divisible: int) -> List:
  return list(
      filter(
          lambda num: num % divisible == 0 and num % not_divisible <
          not_divisible, range(start, finish + 1)))


nums = pro_division(divisible=7, not_divisible=5, start=2000, finish=3200)
print(nums)
