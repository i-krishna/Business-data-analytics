# Calculate the number of ways to form a diverse deputation of 3 members (at least one man and one woman) from m men and w women.

import math

def diverseDeputation(m, w):
    # If there are less than 1 man or 1 woman, it's impossible to form a diverse deputation
    if m < 1 or w < 1:
        return 0

    # Total ways to select any 3 members from m + w
    total_combinations = math.comb(m + w, 3)

    # Ways to select 3 men (violates diversity rule)
    men_only_combinations = math.comb(m, 3) if m >= 3 else 0

    # Ways to select 3 women (violates diversity rule)
    women_only_combinations = math.comb(w, 3) if w >= 3 else 0

    # Valid combinations are total minus invalid (men-only and women-only)
    valid_combinations = total_combinations - men_only_combinations - women_only_combinations

    return valid_combinations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    m = int(input().strip())
    w = int(input().strip())

    result = diverseDeputation(m, w)

    fptr.write(str(result) + '\n')
    fptr.close()
