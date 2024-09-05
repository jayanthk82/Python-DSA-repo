class postfix:
    def __init__(self, expression):
        self.expression = expression
        self.stack = []
        self.top = -1
        self.elements = []
        self.solution()
        self.display()


    def precedence(self, char):
        if char == '-':
            return 1
        if char == '+':
            return 2
        if char == '/':
            return 3
        if char == '*':
            return 4

    def solution(self):
        count =0
        for i in self.expression:
            if(count==0 and (i == '-')):
                self.elements.append(i)
            elif i == '(':
                self.stack.append(i)
                self.top += 1
            elif i == ')':
                while self.stack[self.top] != '(':
                    temp = self.stack.pop()
                    self.top -= 1
                    self.elements.append(temp)
                self.stack.pop()  
                self.top -= 1
            elif i == '+' or i == '-' or i == '*' or i == '/':
                if self.top == -1 or self.stack[self.top] == '(':
                    self.stack.append(i)
                    self.top += 1
                elif self.precedence(i) > self.precedence(self.stack[self.top]):
                    self.stack.append(i)
                    self.top += 1
                else:
                    while self.top != -1 and self.stack[self.top] != '(' and self.precedence(i) <= self.precedence(self.stack[self.top]):
                        temp = self.stack.pop()
                        self.top -= 1
                        self.elements.append(temp)
                    self.stack.append(i)
                    self.top += 1
            else:
                self.elements.append(i)
            count +=1
        while self.top != -1:
            temp = self.stack.pop()
            self.top -= 1
            self.elements.append(temp)
   
    def display(self):
        print("\nYour infix notation    ",self.expression)
        print('\nYour postfix notation  ',self.elements)
Expression = input('Enter expression   ')
obj = postfix(Expression)
