class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(s + '\0' for s in strs)

    def decode(self, s: str) -> List[str]:
        return s.split('\0')[:-1]   # drop the empty piece after the final '\0'