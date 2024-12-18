from collections import defaultdict

family_tree = defaultdict(list)
parents = {}

while True:
    line = input().strip()
    if line == "***":
        break
    child, parent = line.split()
    family_tree[parent].append(child)  
    parents[child] = parent           

def count_descendants(person):
    if person not in family_tree:
        return 0
    count = len(family_tree[person])
    for child in family_tree[person]:
        count += count_descendants(child)
    return count

def count_generations(person):
    if person not in family_tree:
        return 0
    max_generation = 0
    for child in family_tree[person]:
        max_generation = max(max_generation, count_generations(child))
    return max_generation + 1

while True:
    line = input().strip()
    if line == "***":
        break
    cmd, person = line.split()
    if cmd == "descendants":
        print(count_descendants(person))
    elif cmd == "generation":
        print(count_generations(person))
