class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        zeros = []
        total_product = 1
        temp_product = 1
        for i,j in enumerate(nums):
            if j == 0:
                zeros.append(i)
                continue
            else:
                total_product *= j
        
        for a in nums:
            if len(zeros) > 1:
                return [0] * len(nums)
            if zeros:
                if a == 0:
                    res.append(total_product)
                else:
                    res.append(0)
            else:
                res.append(int(total_product / a))
        return res


        