class Solution:
    def calculate(self, s: str) -> int:
        curNumber = 0
        oper = '+'
        curChar = ''
        stack = []
        n = len(s)

        for i, c in enumerate(s):
            if c.isdigit():
                curNumber = curNumber * 10 + int(c)
            if (not c.isdigit() and c != ' ') or i == n - 1:
                if oper == '+':
                    stack.append(curNumber)
                elif oper == '-':
                    stack.append(-curNumber)
                elif oper == '*':
                    stack.append(stack.pop() * curNumber)
                else:
                    prevNumber = stack.pop()
                    stack.append(int(prevNumber/curNumber)) 
                oper = c
                curNumber = 0
        
        return sum(stack)