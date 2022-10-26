from timeit import default_timer as timer
from memory_profiler import profile

@profile
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


start = timer()
print(fib(10))
end = timer()
print(end - start)

