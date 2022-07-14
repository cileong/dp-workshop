def recursive_fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)
