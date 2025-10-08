from itertools import combinations
import random

def arrange_all_combinations(n, s):
    s = list(s)
    s_sorted = sorted(s)
    results = []

    def backtrack(available, used, current_rows, next_length):
        if not available or next_length > n:
            remaining = ''.join([c for c in s if c not in used])
            results.append((current_rows[:], remaining))
            return

        for combo in combinations(available, next_length):
            new_row = ''.join(sorted(combo))
            new_used = used | set(combo)
            new_available = [c for c in available if c not in combo]
            backtrack(new_available, new_used, current_rows + [new_row], next_length + 1)

        remaining = ''.join([c for c in s if c not in used])
        results.append((current_rows[:], remaining))

    backtrack(s_sorted, set(), [], 1)

    unique_results = []
    for rows, remaining in results:
        if (rows, remaining) not in unique_results:
            unique_results.append((rows, remaining))
            
    min_remaining_len = min(len(r[1]) for r in unique_results)
    best_result = [r for r in unique_results if len(r[1]) == min_remaining_len]
    # print(unique_results)
    
    return best_result

all_results = arrange_all_combinations(5, "edbca")

random_answer = random.choice(all_results)
print("Output")
for x in random_answer[0]:
    print(x)
print("remaining = " , ''.join(set(random_answer[1])))