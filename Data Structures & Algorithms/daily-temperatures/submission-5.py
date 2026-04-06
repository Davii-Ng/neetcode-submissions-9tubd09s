class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        warmstack = []
        out = [0] * n
        for i in range(n):
                while warmstack and  temperatures[i] > temperatures[warmstack[-1]]:
                    a = warmstack.pop()
                    out[a]  = i - a
                    
                warmstack.append(i)
        return out


            
        