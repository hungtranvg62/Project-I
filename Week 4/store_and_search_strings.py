def main():
    database = set()  # Use a set for efficient lookup and insertion.
    
    # Read the first block of keys.
    while True:
        key = input().strip()
        if key == '*':  # End of the first block.
            break
        database.add(key)
    
    # Read the second block of commands.
    while True:
        command = input().strip()
        if command == '***':  # End of the second block.
            break
        
        cmd, key = command.split()
        
        if cmd == 'find':
            if key in database:
                print(1)
            else:
                print(0)
        elif cmd == 'insert':
            if key in database:
                print(0)
            else:
                database.add(key)
                print(1)

# Call the main function to execute the program.
main()
