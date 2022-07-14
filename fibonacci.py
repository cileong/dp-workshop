def recursive_fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)


def dp_fib(n: int) -> int:
    memo = [0] * max(n, 2)
    
    # Base case
    memo[0] = 0
    memo[1] = 1

    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[-1]


def optimised_dp_fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
