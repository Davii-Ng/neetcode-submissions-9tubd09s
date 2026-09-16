class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hashset = set()

        for num in nums:
            hashset.add(num)

        return len(hashset) != n