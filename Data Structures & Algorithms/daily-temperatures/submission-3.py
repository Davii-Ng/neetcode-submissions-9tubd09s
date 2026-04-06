class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        warmstack = []
        out = [0] * n
        for i, j in enumerate(temperatures):
                while warmstack and j > warmstack[-1][1]:
                    out[warmstack[-1][0]]  = i - warmstack[-1][0]
                    warmstack.pop()
                warmstack.append([i,j])
        return out


            
        