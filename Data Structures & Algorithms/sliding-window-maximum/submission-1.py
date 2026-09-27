from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # indices; their values are decreasing
        ans = []
        for i, x in enumerate(nums):
            if dq and dq[0] <= i - k:          # 1. front left the window
                dq.popleft()
            while dq and nums[dq[-1]] <= x:    # 2. drop useless candidates
                dq.pop()
            dq.append(i)                       # 3. add new one
            if i >= k - 1:                     # window is full
                ans.append(nums[dq[0]])
        return ans