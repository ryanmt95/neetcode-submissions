class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {'(':')', '{':'}', '[':']'}

        stack = deque()
        for char in s:
            if char in brackets:
                stack.append(char)

            else:
                if len(stack) == 0:
                    return False
                openBracket = stack.pop()
                if char != brackets[openBracket]:
                    return False
        
        return len(stack) == 0

