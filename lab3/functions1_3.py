def solve(numheads, numlegs):
    # Assuming only chickens and rabbits, where chickens have 2 legs and rabbits have 4 legs
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
    return None
