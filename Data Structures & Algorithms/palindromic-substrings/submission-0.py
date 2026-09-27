class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Two pointer approach

        First we will start with the index
        As we search for the palindromes, we expand on both sides
        However since "aa" is also considered a palindrom we cannot just naively expand
        We are using the same technique just that we are going to use i and i+1 to ensure even

        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """

        count = 0
        n = len(s)
        def expand(left, right):
            res = 0
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

            return res

        for i in range(n):
            count += expand(i, i)   #Odd sequence
            count += expand(i, i+1) #Even sequence

        return count