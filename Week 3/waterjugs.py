from collections import deque
import math

def min_steps_to_get_c(a, b, c):
    # If c is greater than the capacity of both jugs or not divisible by gcd, there's no solution
    if c > max(a, b) or c % math.gcd(a, b) != 0:
        return -1

    # BFS Initialization
    queue = deque([(0, 0, 0)])  # Each element in the queue is (jug_a, jug_b, steps)
    visited = set([(0, 0)])  # Set to keep track of visited states (jug_a, jug_b)

    while queue:
        jug_a, jug_b, steps = queue.popleft()

        # If either jug has exactly c liters, return the number of steps
        if jug_a == c or jug_b == c:
            return steps

        # Possible actions
        next_states = [
            (a, jug_b),  # Fill jug a
            (jug_a, b),  # Fill jug b
            (0, jug_b),  # Empty jug a
            (jug_a, 0),  # Empty jug b
            (jug_a - min(jug_a, b - jug_b), jug_b + min(jug_a, b - jug_b)),  # Pour from a to b
            (jug_a + min(jug_b, a - jug_a), jug_b - min(jug_b, a - jug_a))   # Pour from b to a
        ]

        # Explore the next states
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state[0], state[1], steps + 1))

    # If no solution is found, return -1
    return -1

# Input
a, b, c = map(int, input().split())

# Output the result
print(min_steps_to_get_c(a, b, c))
