'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
'''
class Solution(object):
    operators = set(["+", "-", "*", "/"])
    def evalRPN(self, tokens, stack=None, i=0):
        """
        :type tokens: List[str]
        :rtype: int
        """

        if stack == None:
            stack = []
        elif i >= len(tokens):
            return int(stack.pop())
        
        stack.append(tokens[i])

        if stack[-1] in self.operators:
            operator = stack.pop()
            y = int(stack.pop())
            x = int(stack.pop())
            
            if operator ==  "+":
                result = x+y
            elif operator ==  "-":
                result = x-y
            elif operator ==  "*":
                result = x*y
            elif operator ==  "/":
                result = float(x) / float(y)
                result = math.floor(result) if result > 0 else math.ceil(result)
            stack.append(result)       

        return self.evalRPN(tokens, stack, i+1)