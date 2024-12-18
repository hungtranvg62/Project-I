'''
Description
Data about sales in an e-commerce company (the e-commerce company has several shops) consists a sequence of lines, each line (represents an order) has the following information:
            <CustomerID> <ProductID> <Price> <ShopID> <TimePoint>
in which the customer <CustomerID> buys a product <ProductID> with price <Price> at the shop <ShopID> at the time-point <TimePoint>
<CustomerID>: string of length from 3 to 10
<ProductID>: string of length from 3 to 10
<Price>: a positive integer from 1 to 1000
<ShopID>: string of length from 3 to 10
<TimePoint>: string representing time-point with the format HH:MM:SS (for example, 09:45:20 means the time-point 9 hour 45 minutes 20 seconds)


Perform a sequence of queries of following types:
?total_number_orders: return the total number of orders
?total_revenue: return the total revenue the e-commerce company gets
?revenue_of_shop <ShopID>: return the total revenue the shop <ShopID> gets 
?total_consume_of_customer_shop <CustomerID> <ShopID>: return the total revenue the shop <ShopID> sells products to customer <CustomerID> 
?total_revenue_in_period <from_time> <to_time>: return the total revenue the e-commerce gets of the period from <from_time> to <to_time> (inclusive)

Input
The input consists of two blocks of data:
The first block is the operational data, which is a sequence of lines (number of lines can be upto 100000), each line contains the information of a submission with above format 
The first block is terminated with a line containing the character #
The second block is the query block, which is a sequence of lines (number of lines can be upto 100000), each line is a query described above
The second block is terminated with a line containing the character #

Output
Write in each line, the result of the corresponding query 

Example
Input
C001 P001 10 SHOP001 10:30:10
C001 P002 30 SHOP001 12:30:10
C003 P001 40 SHOP002 10:15:20
C001 P001 80 SHOP002 08:40:10
C002 P001 130 SHOP001 10:30:10
C002 P001 160 SHOP003 11:30:20
#
?total_number_orders
?total_revenue
?revenue_of_shop SHOP001
?total_consume_of_customer_shop C001 SHOP001 
?total_revenue_in_period 10:00:00 18:40:45
#


Output 
6
450
170
40
370
'''

import sys
from bisect import bisect_left, bisect_right  # Import binary search utilities for efficient range queries

# Define input and output methods
input = sys.stdin.read
output = sys.stdout.write

def time_to_sec(time):
    # Convert time in HH:MM:SS format to seconds for easier range comparisons
    h, m, s = map(int, time.split(':'))
    return 3600 * h + 60 * m + s

# Initialize data structures
db = []  # List to store transaction records
total_orders = 0  # Counter for total number of orders
total_revenue = 0  # Counter for total revenue
shop_revenue = {}  # Dictionary to store revenue per shop
customer_shop_revenue = {}  # Dictionary to store customer-specific revenue per shop

# Read and parse the input data
data = input().splitlines()  # Read input lines into a list of strings

i = 0
while data[i] != "#":  # Loop until the end of the transaction data block
    # Parse a single transaction
    c_id, p_id, price, s_id, time = data[i].split()
    price = int(price)  # Convert price to an integer
    sec = time_to_sec(time)  # Convert transaction time to seconds
    
    # Append transaction details to the database
    db.append([c_id, p_id, price, s_id, sec])
    
    # Update total orders and total revenue
    total_orders += 1
    total_revenue += price
    
    # Update shop-specific revenue
    if s_id not in shop_revenue:
        shop_revenue[s_id] = 0
    shop_revenue[s_id] += price
    
    # Update customer-specific revenue for the shop
    if c_id not in customer_shop_revenue:
        customer_shop_revenue[c_id] = {}
    if s_id not in customer_shop_revenue[c_id]:
        customer_shop_revenue[c_id][s_id] = 0
    customer_shop_revenue[c_id][s_id] += price

    i += 1  # Move to the next line

# Sort the database by transaction time (in seconds) for range queries
db.sort(key=lambda x: x[4])

# Compute cumulative revenue for efficient range queries
cumulative_revenue = []
current_sum = 0  # Accumulator for the revenue sum
for record in db:
    current_sum += record[2]  # Add the price of the current transaction
    cumulative_revenue.append(current_sum)  # Append the current sum to the cumulative revenue list

i += 1  # Skip the "#" line separating data and queries
res = []  # List to store the results of queries

# Process each query
while data[i] != "#":  # Loop until the end of the query block
    command = data[i].split()  # Split the query into parts
    
    if command[0] == '?total_number_orders':
        # Query: Total number of orders
        res.append(f"{total_orders}\n")
    
    elif command[0] == '?total_revenue':
        # Query: Total revenue of all transactions
        res.append(f"{total_revenue}\n")
    
    elif command[0] == '?revenue_of_shop':
        # Query: Total revenue of a specific shop
        shop_id = command[1]
        res.append(f"{shop_revenue.get(shop_id, 0)}\n")
    
    elif command[0] == '?total_consume_of_customer_shop':
        # Query: Total revenue for a specific customer at a specific shop
        customer_id = command[1]
        shop_id = command[2]
        if customer_id in customer_shop_revenue and shop_id in customer_shop_revenue[customer_id]:
            res.append(f"{customer_shop_revenue[customer_id][shop_id]}\n")
        else:
            res.append("0\n")
    
    elif command[0] == '?total_revenue_in_period':
        # Query: Total revenue within a specific time period
        start_time = time_to_sec(command[1])  # Convert start time to seconds
        end_time = time_to_sec(command[2])  # Convert end time to seconds
        
        # Find the indices of transactions within the specified time range
        start_idx = bisect_left([rec[4] for rec in db], start_time)  # Index of the first transaction >= start_time
        end_idx = bisect_right([rec[4] for rec in db], end_time) - 1  # Index of the last transaction <= end_time
        
        if start_idx <= end_idx:  # If there are transactions in the range
            result = cumulative_revenue[end_idx]  # Get cumulative revenue up to end_idx
            if start_idx > 0:  # Exclude revenue before start_idx
                result -= cumulative_revenue[start_idx - 1]
            res.append(f"{result}\n")
        else:
            res.append("0\n")  # No transactions in the range
    
    i += 1  # Move to the next query

# Output all results at once
output("".join(res))

# import sys
# from bisect import bisect_left, bisect_right

# def time_to_sec(time):
#     """Convert time in HH:MM:SS format to seconds."""
#     h, m, s = map(int, time.split(':'))
#     return 3600 * h + 60 * m + s

# def main():
#     input = sys.stdin.read  # Read input from standard input
#     output = sys.stdout.write  # Write output to standard output
    
#     # Initialize data structures
#     db = []  # List to store transaction records
#     total_orders = 0  # Counter for total number of orders
#     total_revenue = 0  # Counter for total revenue
#     shop_revenue = {}  # Dictionary to store revenue per shop
#     customer_shop_revenue = {}  # Dictionary to store customer-specific revenue per shop
    
#     data = input().splitlines()  # Read input lines into a list of strings
    
#     # Parse transaction data
#     i = 0
#     while data[i] != "#":
#         # Parse a single transaction
#         c_id, p_id, price, s_id, time = data[i].split()
#         price = int(price)  # Convert price to an integer
#         sec = time_to_sec(time)  # Convert transaction time to seconds
        
#         # Append transaction details to the database
#         db.append([c_id, p_id, price, s_id, sec])
        
#         # Update total orders and total revenue
#         total_orders += 1
#         total_revenue += price
        
#         # Update shop-specific revenue
#         if s_id not in shop_revenue:
#             shop_revenue[s_id] = 0
#         shop_revenue[s_id] += price
        
#         # Update customer-specific revenue for the shop
#         if c_id not in customer_shop_revenue:
#             customer_shop_revenue[c_id] = {}
#         if s_id not in customer_shop_revenue[c_id]:
#             customer_shop_revenue[c_id][s_id] = 0
#         customer_shop_revenue[c_id][s_id] += price
        
#         i += 1  # Move to the next line
    
#     # Sort the database by transaction time (in seconds) for range queries
#     db.sort(key=lambda x: x[4])
    
#     # Compute cumulative revenue for efficient range queries
#     cumulative_revenue = []
#     current_sum = 0  # Accumulator for the revenue sum
#     for record in db:
#         current_sum += record[2]  # Add the price of the current transaction
#         cumulative_revenue.append(current_sum)  # Append the current sum to the cumulative revenue list
    
#     i += 1  # Skip the "#" line separating data and queries
#     res = []  # List to store the results of queries
    
#     # Process queries
#     while data[i] != "#":  # Loop until the end of the query block
#         command = data[i].split()  # Split the query into parts
        
#         if command[0] == '?total_number_orders':
#             # Query: Total number of orders
#             res.append(f"{total_orders}\n")
        
#         elif command[0] == '?total_revenue':
#             # Query: Total revenue of all transactions
#             res.append(f"{total_revenue}\n")
        
#         elif command[0] == '?revenue_of_shop':
#             # Query: Total revenue of a specific shop
#             shop_id = command[1]
#             res.append(f"{shop_revenue.get(shop_id, 0)}\n")
        
#         elif command[0] == '?total_consume_of_customer_shop':
#             # Query: Total revenue for a specific customer at a specific shop
#             customer_id = command[1]
#             shop_id = command[2]
#             if customer_id in customer_shop_revenue and shop_id in customer_shop_revenue[customer_id]:
#                 res.append(f"{customer_shop_revenue[customer_id][shop_id]}\n")
#             else:
#                 res.append("0\n")
        
#         elif command[0] == '?total_revenue_in_period':
#             # Query: Total revenue within a specific time period
#             start_time = time_to_sec(command[1])  # Convert start time to seconds
#             end_time = time_to_sec(command[2])  # Convert end time to seconds
            
#             # Find the indices of transactions within the specified time range
#             start_idx = bisect_left([rec[4] for rec in db], start_time)  # Index of the first transaction >= start_time
#             end_idx = bisect_right([rec[4] for rec in db], end_time) - 1  # Index of the last transaction <= end_time
            
#             if start_idx <= end_idx:  # If there are transactions in the range
#                 result = cumulative_revenue[end_idx]  # Get cumulative revenue up to end_idx
#                 if start_idx > 0:  # Exclude revenue before start_idx
#                     result -= cumulative_revenue[start_idx - 1]
#                 res.append(f"{result}\n")
#             else:
#                 res.append("0\n")  # No transactions in the range
        
#         i += 1  # Move to the next query
    
#     # Output all results at once
#     output("".join(res))

# if __name__ == "__main__":
#     main()  # Call the main function to execute the program

