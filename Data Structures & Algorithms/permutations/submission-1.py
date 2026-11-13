class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []
        n = len(nums)

        def backtrack(curr):
            if len(curr) == n:
                res.append(curr[:])
                return 

            for i in range(n):
                if nums[i] in curr:
                    continue
                
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()

        backtrack(curr)
        return res