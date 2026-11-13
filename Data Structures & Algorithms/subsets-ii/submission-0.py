class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        n = len(nums)
        nums.sort()

        def backtrack(i , curr):
            res.append(curr[:])
            

            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                curr.append(nums[j])
                backtrack(j+1, curr)
                curr.pop()


        backtrack(0, curr)
        return res