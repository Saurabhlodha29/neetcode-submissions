class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = list()
        start = {'(','{','['}

        for b in s:
            if b in start:
                stack.append(b)

            elif b == ')':
                if len(stack) == 0:
                    return False
                elif stack[-1] != '(':
                    return False
                stack.pop()

            elif b == '}':
                if len(stack) == 0:
                    return False
                elif stack[-1] != '{':
                    return False
                stack.pop()

            elif b == ']':
                if len(stack) == 0:
                    return False
                elif stack[-1] != '[':
                    return False
                stack.pop()

        return len(stack) == 0 