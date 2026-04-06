class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmstack = []
        out = [0 for _ in range(len(temperatures))]
        for i, j in enumerate(temperatures):
            if not warmstack:
                warmstack.append([i , j])
            else:
                if j > warmstack[-1][1]:
                    while warmstack and j > warmstack[-1][1]:
                        out[warmstack[-1][0]]  = i - warmstack[-1][0]
                        warmstack.pop()
                    
                    warmstack.append([i,j])
                else:
                    warmstack.append([i,j])
                    out[i] = 0
        return out


            
        