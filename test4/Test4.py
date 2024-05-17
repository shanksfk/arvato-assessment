"""
    FILL IN THIS CODE

    Given a string containing arithmetic expression, your task is to evaluate it.
    Each operand involved is an integer and following are the ONLY known operators
    that you must handle in order of its precedence

    1. bracket, ()
    2. power, ^
    3. multiplication and division, * /
    4. addition and subtraction, + -

    Requirements:
     - You are not allowed to use any scripting engine to evaluate the expression; Python eval() is prohibited.
     - You are required to write unit tests

    Refer to the following sample input and output for your test cases
    Sample input     Sample Output
    5                5
    10+3*2-1         15
    10*2^4^2         2560
    5*5-50           -25
    5*4/(4-2)        10
    4+3-             INVALID

"""
import unittest

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def __len__(self):
        return len(self.items)


def infix_to_postfix(expression):
    precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    stack = Stack()
    postfix = []
    tokens = list(expression)

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.isdigit():
            num = token
            while (i + 1 < len(tokens)) and tokens[i + 1].isdigit():
                i += 1
                num += tokens[i]
            postfix.append(num)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = stack.pop()
        else:
            while (not stack.is_empty()) and (precedence[stack.peek()] >= precedence[token]):
                postfix.append(stack.pop())
            stack.push(token)
        i += 1

    while not stack.is_empty():
        postfix.append(stack.pop())
    return postfix


def evaluate_postfix(postfix):
    stack = Stack()
    for token in postfix:
        if token.isdigit():
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(operand1, operand2, token)
            stack.push(result)
    return stack.pop()


def perform_operation(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '^':
        return operand1 ** operand2
    else:
        raise ValueError("Invalid operator")


def evaluate_input(expression):
    try:
        postfix_expr = infix_to_postfix(expression)
        return evaluate_postfix(postfix_expr)
    except (IndexError, ValueError):
        return "INVALID"


class TestArithmeticExpressionEvaluation(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(evaluate_input("5"), 5)

    def test_basic_operations(self):
        self.assertEqual(evaluate_input("10+3*2-1"), 15)
        self.assertEqual(evaluate_input("5*5-50"), -25)
        self.assertEqual(evaluate_input("5*4/(4-2)"), 10)

    def test_exponentiation(self):
        self.assertEqual(evaluate_input("10*2^4^2"), 2560)

    def test_invalid_expression(self):
        self.assertEqual(evaluate_input("4+3-"), "INVALID")


if __name__ == '__main__':
    unittest.main()
