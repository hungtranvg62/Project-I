'''
Problem: Week 5 - Hamiton Cycle

Description
Given an undirected graph G = (V,E). Write a program to check if G is a Hamiltonian graph.
Input
Line 1: a positive integer T (number of graphs)
Subsequent lines are information about T graphs, each has the following format:
Line 1: n and m (number of nodes and edges)
Line i+1 (i = 1, 2, ..., m): u and v : two end points of the ith edge
Output
In the i
th
 line, write 1 if the corresponding is a Hamiltonian graph, and write 0, otherwise
Example
Input
2
5 5
1 2
1 3
2 4
2 5
3 5
7 13
1 3
1 5
1 7
2 4
2 5
2 6
3 4
3 5 
3 7
4 6
4 7
5 7
6 7

Output
0
1
'''

def is_hamiltonian(graph, n):
    # Hàm kiểm tra chu trình Hamilton bằng cách quay lui
    path = [-1] * n
    
    # Bắt đầu từ đỉnh 0 (có thể chọn bất kỳ đỉnh nào làm điểm bắt đầu)
    path[0] = 0
    
    def hamiltonian(pos):
        # Nếu tất cả các đỉnh đã được đi qua
        if pos == n:
            # Kiểm tra xem có cạnh nối từ đỉnh cuối đến đỉnh đầu không
            return path[pos - 1] in graph[path[0]]
        
        # Thử đi qua các đỉnh
        for v in range(1, n):
            if v not in path[:pos] and v in graph[path[pos - 1]]:
                path[pos] = v
                if hamiltonian(pos + 1):
                    return True
                path[pos] = -1
        return False
    
    return hamiltonian(1)

def process_graphs():
    # Đọc số lượng đồ thị
    T = int(input())
    
    results = []
    
    for _ in range(T):
        # Đọc số đỉnh và số cạnh
        n, m = map(int, input().split())
        
        # Xây dựng danh sách kề cho đồ thị
        graph = [[] for _ in range(n)]
        
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        
        # Kiểm tra xem đồ thị có phải là Hamiltonian không
        if is_hamiltonian(graph, n):
            results.append(1)
        else:
            results.append(0)
    
    # In kết quả
    for result in results:
        print(result)

# Gọi hàm xử lý
process_graphs()
