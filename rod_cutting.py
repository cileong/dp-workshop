"""
The Rod Cutting Problem.

Given a rod of length n inches and a table of prices p_i for
i = 0, 1, 2, ... n, determine the maximum revenue r_n
obtainable by cutting up the rod and selling the pieces.
"""


def cut_rod(prices: list[float]) -> float:
    N = len(prices)

    # revenue[l] = maximum revenue of rod with length l.
    revenue = [0] * N
    
    # Fill up the memo bottom up.
    for rod_length in range(1, N):

        # Try out every possible fixed length, keep the one
        # that generates the most revenue for the current
        # rod length.
        for fixed_length in range(1, rod_length + 1):

            remaining_length = rod_length - fixed_length

            revenue[rod_length] = max(
                prices[fixed_length] + revenue[remaining_length],
                revenue[rod_length]
            )

    # Return the maximum revenue that can be generated from
    # cutting a rod of length N.
    return revenue[-1]
