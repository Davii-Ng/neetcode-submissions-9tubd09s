class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        
        hashset = set()
        
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        return False