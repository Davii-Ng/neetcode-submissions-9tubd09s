class Solution:
    def rob(self, nums: List[int]) -> int:        

        def _helper(nums):
            rob1, rob2 = 0, 0 
            for n in nums:
                newrob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = newrob
            return rob2

        return max(_helper(nums[1:]), _helper(nums[:-1]), nums[0]) 
        