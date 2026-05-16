class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}
        for i, j in enumerate(nums):
            
            if target - j in find:
                return [find[target-j], i]
            find[j] = i