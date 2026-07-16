class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r, target):
            while l <= r:
                mid = ( l + r ) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    l =  mid + 1
                if nums[mid] > target:
                    r = mid - 1
            return -1 

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l
        result = binary_search(0, pivot - 1, target)
        if result != -1:
            return result
        return binary_search(l, len(nums)-1 , target)