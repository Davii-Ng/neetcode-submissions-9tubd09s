class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Brute Force Solution

        Cast palindrome + sliding window on each substring

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        ans = 0

        def palindrome(t):
            return t == t[::-1]
        
        n = len(s)
        for i in range(n):
            j = i
            temp = ""
            while j < n:
                temp += s[j]
                ans += 1 if palindrome(temp) else 0
                j += 1

        return ans

