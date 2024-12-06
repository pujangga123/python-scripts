import random

banyak = int(input("Banyak lemparan:"))

n = 1
while n <= banyak:
    print(random.randint(1,11), end=",")
    n = n + 1