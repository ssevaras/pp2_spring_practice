from itertools import permutations

def print_permutations(input_str):
    for perm in permutations(input_str):
        print("".join(perm))
