import time
import random


t1 = time.time()
lst1 = [random.randint(0, 100) for _ in range(10000000)]
t2 = time.time()

print(t2 - t1)

t1 = time.time()
lst2 = []
for _ in range(10000000):
    lst2.append(random.randint(0, 100))
t2 = time.time()

print(t2 - t1)
