import re


def evaluate_expr(expression):
    # Convert the expression to a list of tokens
    tokens = re.findall(r'[-+]?\d*.?\d+|\S', expression)

    # Stack to store operands and operators
    operand_stack = []
    operator_stack = []

    for token in tokens:
        if token.isdigit():  # If token is an   operand, add it to the operand stack
            operand_stack.append(float(token))
        elif token in ('+', '-', '*', '/'):  # If   token is an operator,
            # pop two operands from the stack
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            # Apply the operator and push the   result back to the stack
            if token == '+':
                operand_stack.append(op2 + op1)
            elif token == '-':
                operand_stack.append(op2 - op1)
            elif token == '*':
                operand_stack.append(op2 * op1)
            elif token == '/':
                operand_stack.append(op2 / op1)

        elif token == '(':  # If token is an    opening parenthesis, add it to the     operator stack
            operator_stack.append(token)
        elif token == ')':  # If token is a     closing parenthesis,
            # process the operators in the stack    until the matching '(' is found
            while operator_stack[-1] != '(':
                op1 = operand_stack.pop()
                op2 = operand_stack.pop()
                operator = operator_stack.pop()
                if operator == '+':
                    operand_stack.append(op2 + op1)
                elif operator == '-':
                    operand_stack.append(op2 - op1)
                elif operator == '*':
                    operand_stack.append(op2 * op1)
                elif operator == '/':
                    operand_stack.append(op2 / op1)
            operator_stack.pop()  # Remove the  opening parenthesis

    # At this point, there should beonly   one   element in the operandstack,
    # which is the final result.
    return operand_stack.pop()


# Test the function
expr = '3 + 5 * 2 - ( 4 / 2 )'
result = evaluate_expr(expr)
print(result)
