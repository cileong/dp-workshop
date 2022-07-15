"""
The n-th Fibonacci Number Problem.

Given a number n, compute the n-th term of the Fibonacci
series. The n-th term of the Fibonacci series, fib(n)
is defined by:

fib(n) = {
    0                      if n = 0,
    1                      if n = 1,
    fib(n-1) + fib(n-2)    otherwise.
}
"""


def recursive_fib(n: int) -> int:
    """
    The most intuitive, math-y way, but the most time and
    space inefficient.

    For example,
    call fib(10), and it calls fib(9) and fib(8), ...
    call fib(9) , and it calls fib(8) and fib(7), ...
    Notice that fib(8) is computed repeatedly.

    Due to repeated computations, this costs O(2^n) time.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)


def dp_fib(n: int) -> int:
    """
    Knowing this is a linear problem and there are overlapping
    subproblems, we can use memoization to improve the runtime.
    """
    # At least create two spaces to store the base case.
    memo = [0] * max(n+1, 2)
    
    # Base case
    memo[0] = 0
    memo[1] = 1

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]


def optimised_dp_fib(n: int) -> int:
    """
    Notice in the previous implementation, the only parts
    of memo required to compute for the current iteration,
    at any iteration, are memo[i-1] and memo[i-2].

    As only two numbers have to be 'remembered', we can
    replaced the array with a list to save more space. This
    cuts the auxiliary space complexity to O(1).
    """
    # a = memo[i-1]
    # b = memo[i-2]
    # Before any iterations, this is the base case, so:
    # a = fib(0),
    # b = fib(1).
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a+b
    
    return a
