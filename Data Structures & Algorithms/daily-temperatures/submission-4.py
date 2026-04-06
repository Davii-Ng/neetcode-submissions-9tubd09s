class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        warmstack = []
        out = [0] * n
        for i, j in enumerate(temperatures):
                while warmstack and j > warmstack[-1][1]:
                    a = warmstack.pop()
                    out[a[0]]  = i - a[0]
                    
                warmstack.append([i,j])
        return out


            
        