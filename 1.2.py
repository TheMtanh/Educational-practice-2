def combinationSum2(candidates, target):
    result = []
    candidates.sort()

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:
                break
            backtrack(i + 1, path + [candidates[i]], remaining - candidates[i])

    backtrack(0, [], target)
    return result


candidates = [2, 5, 2, 1, 2]
target = 5
print(combinationSum2(candidates, target))
