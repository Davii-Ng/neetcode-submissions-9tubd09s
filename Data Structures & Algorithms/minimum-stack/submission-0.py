class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = None

    def push(self, val: int) -> None:
        return self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
         tmp = []
         mini = self.stack[-1]

         while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())

         while len(tmp):
            self.stack.append(tmp.pop())

         return mini
