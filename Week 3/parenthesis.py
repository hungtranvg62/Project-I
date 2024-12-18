def is_valid_expression(s):
    stack = []
    # Dictionary to match the pairs of brackets
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map.values():  # Opening brackets
            stack.append(char)
        elif char in bracket_map:  # Closing brackets
            if not stack or stack[-1] != bracket_map[char]:
                return 0  # Incorrect expression
            stack.pop()  # Pop the matching opening bracket
        else:
            return 0  # Invalid character
    
    return 1 if not stack else 0  # Stack should be empty if correct

# Input
s = input()

# Output result
print(is_valid_expression(s))
