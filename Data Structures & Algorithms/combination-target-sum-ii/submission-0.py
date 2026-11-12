class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        curr = []
        n = len(candidates)

        def backtrack(i, total):
            if total == target:
                res.append(curr[:])
                return

            for j in range(i, n):
                # Skip duplicate choices at the same level
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                # Since sorted, everything after this is also too large
                if total + candidates[j] > target:
                    break

                curr.append(candidates[j])

                backtrack(j + 1, total + candidates[j])

                curr.pop()

        backtrack(0, 0)

        return res