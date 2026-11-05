class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        numStack = deque()
        operations = set(['*', '/', '+', '-'])

        for token in tokens:
            if token in operations:
                numB = int(numStack.pop())
                num = int(numStack.pop())
                match token:
                    case '*':
                        num *= numB
                    case '/':
                        num /= numB
                    case '+':
                        num += numB
                    case '-':
                        num -= numB
                
                numStack.append(num)
            else:
                numStack.append(token)

        return int(numStack[0])