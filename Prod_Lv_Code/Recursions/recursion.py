'''
Two required parts: base case (stops it) and recursive case (reduces the problem).

2.1 Why recursion breaks in production without care?

 - Python has no tail-call optimization. Deep recursion (~1000 default limit) raises RecursionError.
 - Naive recursion recomputes overlapping subproblems (e.g. plain Fibonacci is O(2^n)).

'''

def factorial(n):
    if n <= 1:                 # base case
        return 1
    return n * factorial(n-1)  # recursive case



'''Memorization fixes with performance problem'''

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


'''

2.3 When to actually use recursion in production ?

 - Tree/graph traversal (file systems, JSON/nested config parsing, org charts)
 - Divide-and-conquer algorithms (merge sort, quicksort)
 - Backtracking (permutations, parsing, constraint search)
 - Not for simple linear iteration — that's just an iterative loop, recursion adds overhead and risk for no benefit.

'''