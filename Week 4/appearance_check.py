def main():
    n = int(input())  # Read the number of elements.
    A = list(map(int, input().split()))  # Read the sequence of integers.
    
    seen = set()  # To store elements that have been encountered.
    
    for i in range(n):
        if A[i] in seen:
            print(1)
        else:
            print(0)
            seen.add(A[i])

# Call the main function to execute the program.
main()
