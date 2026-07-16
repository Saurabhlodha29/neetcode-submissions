import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        ops = {
            "+":operator.add,
            "-":operator.sub,
            "*":operator.mul,
            "/":operator.truediv
        }


        for i in tokens:
            if i in ops:
                op2 = int(stack.pop())
                op1 = int(stack.pop())

                result = int(ops[i](op1,op2))

                stack.append(result)

            else:
                stack.append(i)

        return stack.pop()