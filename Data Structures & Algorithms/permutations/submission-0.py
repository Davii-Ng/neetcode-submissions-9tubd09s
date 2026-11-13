class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        n = len(nums)

        def backtrack(curr, seen):
            if len(curr) == n:
                res.append(curr[:])
                return 

            for i in range(n):
                if nums[i] in seen:
                    continue

                curr.append(nums[i])
                seen.add(nums[i])

                backtrack(curr, seen)

                curr.pop()
                seen.remove(nums[i])


        backtrack([], set())

        return res