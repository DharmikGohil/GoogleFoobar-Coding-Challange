from itertools import combinations

def solution(num_buns, num_required):
    # Case when no bunnies are required to open the cell
    if num_required == 0:
        return [[] for _ in range(num_buns)]

    # Generate all possible keys
    all_keys = list(range(num_buns))
    # Generate combinations of keys for each bunny
    key_combinations = list(combinations(all_keys, num_buns - num_required + 1))

    # Initialize a list to store keys assigned to each bunny
    bunnies_keys = [[] for _ in range(num_buns)]

    # Assign each combination to the corresponding bunnies
    for i, keys in enumerate(key_combinations):
        for key in keys:
            bunnies_keys[key].append(i)

    return bunnies_keys

# # Test cases
# print(solution(4, 4))
# print(solution(5, 3))
# print(solution(2, 1))
