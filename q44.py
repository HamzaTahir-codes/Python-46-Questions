def is_balanced(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


# Test the function
test_cases = ["[]", "][", "[][]", "][[]", "[[][]]", "[]][[]"]
for brackets in test_cases:
    if is_balanced(brackets):
        print(f"{brackets}: OK")
    else:
        print(f"{brackets}: NOT OK")
