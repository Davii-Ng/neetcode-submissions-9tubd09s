class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            print(element)
            if element == "+":
                e1 = stack.pop()
                e2 = stack.pop()
                res = e1 + e2
                stack.append(res)
            elif element == '-':
                e1 = stack.pop()
                e2 = stack.pop()
                res = e2 - e1
                stack.append(res)
            elif element == '*':
                e1 = stack.pop()
                e2 = stack.pop()
                res = e1 * e2
                stack.append(res)
            elif element == '/':
                e1 = stack.pop()
                e2 = stack.pop()
                res = int(e2/e1)
                stack.append(res)
            else:
                stack.append(int(element))

            print(stack)

        return stack[0]