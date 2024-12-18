'''
Problem: Week 4 - Sum pair of sequence equal to a number

Description
Cho dãy a1, a2, ..., an trong đó các phần tử đôi một khác nhau và 1 giá trị nguyên dương M. Hãy đếm số Q các cặp (i,j) sao cho 1 <= i < j <= n và ai + aj = M.

Dữ liệu
Dòng 1: ghi n và M (1 <= n, M <= 1000000)
Dòng 2: ghi a1, a2, ..., an
Kết quả
Ghi ra giá trị Q
Ví dụ
Dữ liệu
5 6
5 2 1 4 3
Kết quả
2
'''

def count_pairs(n, M, arr):
    scanned = set()
    count = 0
    for num in arr:
        if (M - num) in scanned:
            count += 1
        scanned.add(num)
    return count

n, M = map(int, input().split())
arr = list(map(int, input().split()))

print(count_pairs(n, M, arr))
