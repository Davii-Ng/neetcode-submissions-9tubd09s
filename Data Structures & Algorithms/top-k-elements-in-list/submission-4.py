class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
        sortarr = []
        for val in hashmap:
            sortarr.append([val, hashmap[val]])
        # print(sortarr)

        sortarr.sort(key = lambda x : x[1], reverse = True)

        ans = []
        for j in range(k):
            ans.append(sortarr[j][0])

        return ans