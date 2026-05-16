class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        out = []
        for string in strs:
            new = sorted(string)
            new = "".join(new)
            print(new)
            if new not in seen:
                seen[new]  = []
                seen[new].append(string)
            else:
                seen[new].append(string)

        print(seen)
        for array in seen:
            out.append(seen[array])
            

        return out
