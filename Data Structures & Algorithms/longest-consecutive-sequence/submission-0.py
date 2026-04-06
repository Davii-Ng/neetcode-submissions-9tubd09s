class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        store = set(nums)
        streak = 1
        for num in nums:
            temp_streak = 1
            if num + 1 in store:
                while num + 1 in store:
                    temp_streak += 1
                    num += 1
                if temp_streak > streak:
                    streak = temp_streak
        return streak

        