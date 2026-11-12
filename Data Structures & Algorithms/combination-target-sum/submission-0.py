class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        n = len(nums)

        def backtrack(curr, total, i):
            if total == target:
                res.append(curr[:])
                return 

            if total > target:
                return 
            
            for i in range(i, n):
                curr.append(nums[i])

                backtrack(curr, total + nums[i], i)

                curr.pop()

        backtrack([], 0, 0)
        return res

