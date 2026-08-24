class Solution:
    def isOperation(self, token):
        return token in ["+", "-", "/", "*"]

    def doOperation(self, num1, num2, operation):
        if operation == "+":
            return num1 + num2
        if operation == "-":
            return num1 - num2
        if operation == "/":
            return int(num1 / num2)
        if operation == "*":
            return num1 * num2

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for token in tokens:
            if self.isOperation(token):
                num2 = stack.pop()
                num1 = stack.pop()
                result = self.doOperation(num1, num2, token)
                stack.append(result)
            else:
                stack.append(int(token))
    
        return stack[0]
