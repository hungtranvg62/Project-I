def compute_hash_codes(n, m, strings):
    hash_codes = []
    
    for s in strings:
        hash_value = 0
        k = len(s)
        
        for i in range(k):
            # Calculate ASCII value of character s[i] (1-indexed in problem, 0-indexed in Python)
            char_value = ord(s[i])
            # Calculate the contribution of the character to the hash value
            hash_value = (hash_value * 256 + char_value) % m
        
        hash_codes.append(hash_value)
    
    return hash_codes

# Input handling
n, m = map(int, input().split())
strings = [input().strip() for _ in range(n)]

# Compute the hash codes
hash_codes = compute_hash_codes(n, m, strings)

# Output the hash codes
for hash_code in hash_codes:
    print(hash_code)
