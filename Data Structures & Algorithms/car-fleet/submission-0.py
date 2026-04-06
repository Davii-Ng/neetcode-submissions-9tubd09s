class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        time = 0
        stack = []


        sorting = list(zip(position, speed))
        sorting.sort(reverse = True)

        for position, speed in sorting:
            time = (target - position)/ speed
            if not stack:
                stack.append(time)
                continue
            if time > stack[-1]:
                stack.pop()
                ans += 1
                stack.append(time)
        
        return ans + 1

        
        