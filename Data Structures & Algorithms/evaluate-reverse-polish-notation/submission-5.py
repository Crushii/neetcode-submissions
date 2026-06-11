class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ele in tokens:
            if ele not in '+-*/' :
                stack.append(int(ele))
            elif ele == '+':
                val = stack.pop() + stack.pop() 
                stack.append(val)
            elif ele == '-':
                val = stack[-2] - stack[-1] 
                stack.pop()
                stack.pop()
                stack.append(val)
            elif ele == '*':
                val = stack.pop() * stack.pop() 
                stack.append(val)
            elif ele == '/':
                val = stack[-2] / stack[-1] 
                stack.pop()
                stack.pop()
                stack.append(int(val))


        return stack[-1]

        