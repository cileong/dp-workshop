"""
Gusfield's Z-algorithm.

The Z-algorithm, given a string, produces a Z-array. The
Z-array has the same length as the given string. Z[i] stores
the length of the longest substring starting from string[i]
that is a prefix of the string.
"""


def naive_z_algorithm(string: str) -> list[int]:
    N = len(string)

    # Edge case: string is empty.
    if N == 0:
        return []
    
    z = [0] * N

    # Trivially, Z[0] = length of string.
    z[0] = N

    for current in range(1, N):
        i = 0
        j = current

        # Count the number of consecutive characters that agree.
        while j < N and string[i] == string[j]:
            z[current] += 1
            i += 1
            j += 1
    
    return z


def z_algorithm(string: str) -> list[int]:
    N = len(string)

    if N == 0:
        return []

    z = [0] * N

    z[0] = N

    left, right = 0, 0
    for current in range(1, N):
        
        z_box_discovered = False
        previous = current - left
        remaining = right - current

        # Case 1: current char is outside of the Z-box.
        # No knowledge of the current segment, so there is
        # no info in memo.
        # Solution: Compute the Z-value here and find the
        # Z-box (if possible).
        if right < current:
            i = 0
            j = current
            while j < N and string[i] == string[j]:
                z[current] += 1
                i += 1
                j += 1
            z_box_discovered = z[current] > 0
        
        # Case 2: current char is inside the Z-box.

        # Subcase (i): Z[previous] = remaining.
        # No knowledge beyond string[right].
        # Solution:
        # Find how many subsequent char matches beyond
        # string[:right]. The sum of it with the number
        # of remaining char in the current Z-box is the
        # Z-value here. Update the Z-box afterwards.
        elif z[previous] == remaining:
            z[current] = remaining
            i = remaining
            j = right
            while j < N and string[i] == string[j]:
                z[current] += 1
                i += 1
                j += 1
            z_box_discovered = right < current + z[current]

        # Subcase (ii): Z[previous] != remaining
        # If Z[previous] < remaining, the invalid char is inside
        # the Z-box, Z[current] = Z[previous].
        # If Z[previous] > remaining, the char past the current
        # Z-box is the invalid, Z[current] = remaining.
        # Solution: Z[current] is bounded by the smaller of
        # Z[previous] and remaining.
        else:
            z[current] = min(z[previous], remaining)

        # Update the Z-box if a new one is discovered.
        if z_box_discovered:
            left = current
            right = left + z[current]
    
    # Return the Z-array.
    return z
