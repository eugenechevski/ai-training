 def evaluate_expr(expression):
        # Convert the expression to a list of tokens 
    import re
    tokens = re.findall(r'[-+]?\d*.?\d+|\S', expression)

# Stack to store operands and operators 
operand_stack = []
operator_stack = []

for token in tokens:
    if token.isdigit():  # If token is an operand, add it to the operand stack
        operand_stack.append(float(token))
    elif token in ('+', '-', '*', '/'):  # If token is an operator, add it to the operator stack
        operator_stack.append(token)
    elif token == '(':  # If token is an opening parenthesis, push it to the operator stack
        operator_stack.append(token)
    elif token == ')':  # If token is a closing parenthesis, 
        while operator_stack[-1] != '(':  # pop operators until you find the matching '('
            operand1 = operand_stack.pop()
            operand2 = operand_stack.pop()
            operator = operator_stack.pop()
            operand_stack.append(apply_operator(operand2, operand1, operator))
        operator_stack.pop()  # pop the opening parenthesis

# At this point, all parentheses should be removed from the operator stack. 
# Perform the remaining operations from the operator stack.
while operator_stack:
    operand1 = operand_stack.pop()
    operand2 = operand_stack.pop()
    operator = operator_stack.pop()
    operand_stack.append(apply_operator(operand2, operand1, operator))

# Return the final result from the operand stack
return operand_stack.pop()
def apply_operator(operand1, operand2, operator):
    if operator == '+':
        return operand2 + operand1
    elif operator == '-':
        return operand2 - operand1
    elif operator == '*':
        return operand2 * operand1
    elif operator == '/':
        return operand2 / operand1

 #Test cases
 print(evaluate_expr('3 + 5 * 2'))#Output 13.0
 print(evaluate_expr('3 + 5 - 2 * 4'))#Output 3.0
 print(evaluate_expr('2 * (3 + 4)'))#Output 14.0
 print(evaluate_expr('(2 + 3) * (4 -1) '))#Output 15.0
 print(evaluate_expr('10 / (5 + 1)'))#Output 2.0