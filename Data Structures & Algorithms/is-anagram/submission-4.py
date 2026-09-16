class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        n = len(s)

        s = [c for c in s]
        t = [c for c in t]
        s.sort()
        t.sort()

        for i in range(n):
            if s[i] != t[i]:
                return False

        return True