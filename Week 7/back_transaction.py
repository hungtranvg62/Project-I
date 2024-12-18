# '''
# Description
# The data about bank transactions consists of a sequence of transactions: the information of each transaction has the following format:
#                                                                     <from_account>   <to_account>   <money>   <time_point>   <atm>
# In which:
# •	<from_account>: the account from which money is transferred (which is a string of length from 6 to 20 )
# •	<to_account>: the account which receives money in the transaction (which is a string of length from 6 to 20)
# •	<money>: amount of money transferred in the transaction (which is an integer from 1 to 10000)
# •	<time_point>: the time point at which the transaction is performed, it is a string under the format HH:MM:SS  (hour: minute: second)
# •	<atm>: the code of the ATM where the transaction is taken (a string of length from 3 to 10)
# Example: T00112233445 T001234002 2000 08:36:25 BIDV (at the ATM BIDV, account T00112233445 transfers 2000$ to account T001234002 at time point 08:36:25 (08 hour, 36 minutes, 25 seconds) 
# A transaction cycle of length k starting from account a1 is defined to be a sequence of distinct account a1, a2, …, ak  in which there are transactions from account a1 to a2, from a2 to a3, …, from ak to a1.
# Write a program that process the following queries: 
# ?number_transactions: compute the total number of transactions of the data
# ?total_money_transaction: compute the total amount of money of transactions  
# ?list_sorted_accounts: compute the sequence of bank accounts (including sending and receiving accounts) appearing in the transaction (sorted in an increasing (alphabetical) order)  
# ?total_money_transaction_from <account>: compute the total amount of money transferred from the account <account>  
# ?inspect_cycle <account> k : return 1 if there is a transaction cycle of length k, starting from <account>, and return 0, otherwise
# Input (stdin)
# The input consists of 2 blocks of information: the data block and the query block
# •	The data block consists of lines:
# o	Each line contains the information about a transaction described above
# o	The data is terminated by a line containing #
# •	The query block consists of lines:
# o	Each line is a query described above
# o	The query block is terminated by a line containing #

# Output (stdout)
# •	Print to stdout (in each line) the result of each query described above

# Example
# Input
# T000010010 T000010020 1000 10:20:30 ATM1
# T000010010 T000010030 2000 10:02:30 ATM2
# T000010010 T000010040 1500 09:23:30 ATM1
# T000010020 T000010030 3000 08:20:31 ATM1
# T000010030 T000010010 4000 12:40:00 ATM2
# T000010040 T000010010 2000 10:30:00 ATM1
# T000010020 T000010040 3000 08:20:31 ATM1
# T000010040 T000010030 2000 11:30:00 ATM1
# T000010040 T000010030 1000 18:30:00 ATM1
# #
# ?number_transactions
# ?total_money_transaction
# ?list_sorted_accounts
# ?total_money_transaction_from T000010010
# ?inspect_cycle T000010010 3
# #
# Output
# 9
# 19500
# T000010010 T000010020 T000010030 T000010040
# 4500
# 1
# '''

# import sys
# from collections import defaultdict

# def find_cycle(graph, start, k, current, visited, path_length):
#     """Recursive function to find cycles of length k in the transaction graph."""
#     if path_length == k:
#         return current == start
    
#     visited.add(current)
#     for neighbor in graph[current]:
#         if (neighbor != start and neighbor not in visited) or (neighbor == start and path_length == k - 1):
#             if find_cycle(graph, start, k, neighbor, visited, path_length + 1):
#                 return True
#     visited.remove(current)
#     return False

# def main():
#     input = sys.stdin.read
#     output = sys.stdout.write
    
#     # Data structures for processing transactions
#     transactions = []
#     account_money_from = defaultdict(int)
#     all_accounts = set()
#     graph = defaultdict(list)

#     # Read input and parse transactions
#     input_lines = input().strip().splitlines()
#     i = 0
#     while input_lines[i] != '#':
#         from_acc, to_acc, money, time_point, atm = input_lines[i].split()
#         money = int(money)
        
#         # Process transaction
#         transactions.append((from_acc, to_acc, money, time_point, atm))
#         account_money_from[from_acc] += money
#         all_accounts.update([from_acc, to_acc])
#         graph[from_acc].append(to_acc)
        
#         i += 1
#     i += 1  # Skip the `#` line

#     # Process queries
#     while input_lines[i] != '#':
#         query = input_lines[i].split()

#         if query[0] == "?number_transactions":
#             # Total number of transactions
#             output(f"{len(transactions)}\n")

#         elif query[0] == "?total_money_transaction":
#             # Total money transferred
#             total_money = sum(money for _, _, money, _, _ in transactions)
#             output(f"{total_money}\n")

#         elif query[0] == "?list_sorted_accounts":
#             # Sorted list of unique accounts
#             sorted_accounts = sorted(all_accounts)
#             output(" ".join(sorted_accounts) + "\n")

#         elif query[0] == "?total_money_transaction_from":
#             # Total money transferred from a specific account
#             account = query[1]
#             output(f"{account_money_from[account]}\n")

#         elif query[0] == "?inspect_cycle":
#             # Check for cycles of a specific length starting from an account
#             account = query[1]
#             k = int(query[2])
#             visited = set()
#             if find_cycle(graph, account, k, account, visited, 0):
#                 output("1\n")
#             else:
#                 output("0\n")

#         i += 1

# if __name__ == "__main__":
#     main()

import numpy as np
a = np.arange(1, 21)
# YOUR CODE HERE
result = a.reshape(4, 5)
print(result)