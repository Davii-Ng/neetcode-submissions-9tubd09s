class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}
        for i, j in enumerate(nums):
            find[j] = i
        
        for i, j in enumerate(nums):
            if target - j in find and find[target-j] != i:
                return [i, find[target-j]]