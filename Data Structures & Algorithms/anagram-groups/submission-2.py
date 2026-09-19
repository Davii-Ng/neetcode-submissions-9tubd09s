class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            hash_val = [0] * 26
            for c in word:
                hash_val[ord(c)- ord('a')] += 1
            hash_val = tuple(hash_val)
            if hash_val in seen:
                seen[hash_val].append(word)
            else:
                seen[hash_val] = [word]

        ans = []
        for array in seen:
            ans.append(seen[array])
        return ans