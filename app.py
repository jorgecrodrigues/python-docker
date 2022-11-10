import os
import timeit

start = timeit.default_timer()

print(os.getcwd())

for i in range(1000000):
    print(i)

stop = timeit.default_timer()

print('Time: ', stop - start)