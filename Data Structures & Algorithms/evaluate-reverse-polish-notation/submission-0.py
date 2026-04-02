class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evaluate_stack = list()
        for token in tokens:
            if token == "+":
                evaluate_stack.append(evaluate_stack.pop() + evaluate_stack.pop())
            elif token == "-":
                a, b = evaluate_stack.pop(),  evaluate_stack.pop()
                evaluate_stack.append(b - a)
            elif token == "*":
                evaluate_stack.append(evaluate_stack.pop() * evaluate_stack.pop())
            elif token == "/":
                a, b = evaluate_stack.pop(),  evaluate_stack.pop()
                evaluate_stack.append(int(b / a))
            else:
                evaluate_stack.append(int(token))
        return evaluate_stack[0]

        