class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        ans = 0

        for num in set_nums:
            if (num - 1) not in set_nums:
                streak = 1
                while (num + streak) in set_nums:
                    streak += 1

                ans = max(ans, streak)



        return ans


        