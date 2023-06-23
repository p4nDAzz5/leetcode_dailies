class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        opperands = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in opperands:
                stack.append(int(token))
            else:
                if token == "+":
                    tempOne = stack.pop()
                    stack.append(tempOne + stack.pop())
                elif token == "-":
                    tempOne = stack.pop()
                    stack.append(stack.pop() - tempOne)
                elif token == "*":
                    tempOne = stack.pop()
                    stack.append(tempOne * stack.pop())
                elif token == "/":
                    tempOne = stack.pop()
                    stack.append(int((float(stack.pop()) / tempOne)))

        return(stack[0])