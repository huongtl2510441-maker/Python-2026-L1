1.
r = input("Enter circle radius? ")
pi = float(3.14)
print(f"Circle area = {pi * float(r) ** 2}")

2.
Temperature = int(input("Enter the temperature in Celsius? "))
print(f" {Temperature} (C) = {Temperature * 9/5 + 32} (F)")

3.
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Enter a number? "))
if prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is NOT a prime number")

4. 
def perfect(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

n = int(input("Enter a number? "))
if perfect(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is NOT a perfect number")

5.
given_list = ["Pink", "Blue", "White", "Red", "Orange", "Purple"]
color = input("What is your favourite color? ")
if color in given_list:
    index = given_list.index(color)
    print(f"Your favourite color is at index: {index}")
else:
    print("Sorry, I couldn't find your color")


6.
range1 = range(0, 7)
print(list(range1))
range2 = range(1, 11, 3)
print(list(range2))
range3 = range(5, 0, -1) 
print(list(range3))
range4 = range(6, -3, -2)
print(list(range4))


7.
def remove_dollar_sign(s):
  return s.replace("$", "")

8.
def extract_even(l):
  return [num for num in l if num % 2 == 0]


9.
def factorial(n):
  if n == 0 or n == 1:
    return 1
  result = 1
  for i in range(2, n + 1):
    result *= i
  return result

10.
def get_divisors(n):
  divisors = []
  for i in range(1, n + 1):
    if n % i == 0:
       divisors.append(i)
  return divisors

11.
import math
def distance(point1, point2):
  return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


12.
def print_pattern(m, n):
  for i in range(m):
    for j in range(n):
      if i == 0 or i == m - 1 or j == 0 or j == n - 1:
        print("* ", end="")
      else:
        print("  ", end="")
    print()

