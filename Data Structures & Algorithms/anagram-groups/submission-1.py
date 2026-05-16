class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in seen:
                seen[tuple(count)].append(string)
            else:
                seen[tuple(count)] = [string]
        
        return list(seen.values())
