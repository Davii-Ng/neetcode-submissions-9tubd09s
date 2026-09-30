class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums = list(set(nums))
        nums.sort()

        ans = 1
        temp = 1
        n = len(nums)
        for i in range(1,n):

            if nums[i-1] == nums[i] - 1:
                temp += 1
            else:
                temp = 1

            ans = max(ans, temp)

        return ans

        