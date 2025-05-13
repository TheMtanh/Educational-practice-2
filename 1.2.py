from itertools import combinations


def combination(numbers, target):
    result = []
    seen = set()

    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            if sum(combo) == target:
                sorting = tuple(sorted(combo))
                if sorting not in seen:
                    seen.add(sorting)
                    result.append(list(sorting))

    return result

print(combination([2, 5, 2, 1, 2], 5))