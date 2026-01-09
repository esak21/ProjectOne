def check_balanced_parentheses(input_equation: str):
    stack = []
    mapping = {"(": ")", "{": "}", "[": "]"}
    for idx in range(0, len(input_equation)):
        current_value = input_equation[idx]
        if input_equation[idx] == "(" or input_equation[idx] ==" {" or input_equation[idx] == "[":
            stack.append(input_equation[idx])
        else:
            top_rec = stack.pop()
            if (input_equation[idx] == mapping[top_rec] ):
                continue
            else:
                return False
    return len(stack) == 0

def check_balanced_parentheses2(input_equation: str):
    stack = []
    mapping = {"(": ")", "{": "}", "[": "]"}
    for rec in input_equation:
        current_value = rec
        if rec in mapping.keys():
            stack.append(rec)
        else:
            top_rec = stack.pop()
            if rec == mapping[top_rec] :
                continue
            else:
                return False
    return len(stack) == 0


my_equation = "[(())]"

result = check_balanced_parentheses2(my_equation)

print(result)