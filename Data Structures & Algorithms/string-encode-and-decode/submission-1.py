class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result


    def decode(self, s: str) -> List[str]:
        j = 0
        strs = []
        temp = ""
        i = 0
        if len(s) == 0:
            return strs
        while i <= len(s):
            if s[i] == '#':
                wordlength = s[j:i]
                print(wordlength, i)

                temp = s[i+1 : i + int(wordlength) + 1]
                strs.append(temp)
                j = i + int(wordlength) + 1
                i = j + 1
            else:
                i += 1

        return strs



