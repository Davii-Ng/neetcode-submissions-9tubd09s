class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0 

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        slow2 = 0
        while nums[slow2] != nums[fast]:
            slow2 = nums[slow2]
            fast = nums[fast]
        return nums[slow2]


        