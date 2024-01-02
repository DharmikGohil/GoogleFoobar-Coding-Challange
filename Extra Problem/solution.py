from collections import defaultdict

def generate(c1, c2, bitlen):
    # Generate the possible previous state for a 2x2 block
    a = c1 & ~(1 << bitlen)
    b = c2 & ~(1 << bitlen)
    c = c1 >> 1
    d = c2 >> 1
    return (a & ~b & ~c & ~d) | (~a & b & ~c & ~d) | (~a & ~b & c & ~d) | (~a & ~b & ~c & d)

def build_map(n, nums):
    mapping = defaultdict(set)
    nums = set(nums)
    
    # Build mapping of possible transitions
    for i in range(1 << (n + 1)):
        for j in range(1 << (n + 1)):
            generation = generate(i, j, n)
            if generation in nums:
                mapping[(generation, i)].add(j)
    return mapping

def answer(g):
    # Transpose the grid
    g = list(zip(*g))
    nrows = len(g)
    ncols = len(g[0])

    # Convert the grid into numbers
    nums = [sum([1 << i if col else 0 for i, col in enumerate(row)]) for row in g]
    mapping = build_map(ncols, nums)

    preimage = {i: 1 for i in range(1 << (ncols + 1))}
    
    # Update the count of possible previous states
    for row in nums:
        next_row = defaultdict(int)
        for c1 in preimage:
            for c2 in mapping[(row, c1)]:
                next_row[c2] += preimage[c1]
        preimage = next_row
    
    ret = sum(preimage.values())
    return ret

# Example usage:
grid = [
    [True, False, True],
    [False, True, False],
    [True, False, True]
]
result = answer(grid)
print(result)
