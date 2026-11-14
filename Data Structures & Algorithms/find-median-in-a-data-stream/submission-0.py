class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        smallsize = len(self.small)
        largesize = len(self.large)
        
        if smallsize - largesize > 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif largesize - smallsize > 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    
    def findMedian(self) -> float:
        smallsize = len(self.small)
        largesize = len(self.large)

        if smallsize > largesize:
            return -self.small[0]
        elif smallsize < largesize:
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
        
        