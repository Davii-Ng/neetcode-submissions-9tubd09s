class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, j in enumerate(nums):
            if target == j:
                return i
        return -1