class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += string + '\0'
        
        return encoded_str
    def decode(self, s: str) -> List[str]:
        n = len(s)
        decoded = []
        temp = ""
        for i in range(n):
            if s[i] == '\0':
                decoded.append(temp)
                temp = ""
            else:
                temp += s[i]

        return decoded