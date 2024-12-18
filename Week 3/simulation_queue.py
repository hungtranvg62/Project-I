from collections import deque

queue = deque()

while True:
    command = input().strip()
    if command == '#':
        break
    cmd = command.split()
    
    if cmd[0] == "PUSH":
        value = int(cmd[1])
        queue.append(value)
    elif cmd[0] == "POP":
        if queue:
            print(queue.popleft())
        else:
            print("NULL")
