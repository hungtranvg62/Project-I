def stack_operations(operations):
    stack = []
    
    for operation in operations:
        if operation.startswith("PUSH"):
            # Extract the value and push it to the stack
            _, value = operation.split()
            stack.append(int(value))
        elif operation == "POP":
            # Pop the element from the stack and print it, or print NULL if empty
            if stack:
                print(stack.pop())
            else:
                print("NULL")
        elif operation == "#":
            break  # End the sequence when we see the '#' symbol

# Input operations
operations = []
while True:
    command = input().strip()
    operations.append(command)
    if command == "#":
        break

# Perform operations
stack_operations(operations)
