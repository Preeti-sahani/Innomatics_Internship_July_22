# -*- coding: utf-8 -*-
"""Set-Mutations.ipynb"""

'''Task- 
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements from set A.

Input Format :
The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.

Output Format :
Output the sum of elements in set A.
'''

len_set = int(input())

storage = set(map(int, input().split()))

op_len = int(input())

for i in range(op_len):
    operation = input().split()
    if operation[0] == 'intersection_update':
        temp_storage = set(map(int, input().split()))
        storage.intersection_update(temp_storage)
    elif operation[0] == 'update':
        temp_storage = set(map(int, input().split()))
        storage.update(temp_storage)
    elif operation[0] == 'symmetric_difference_update':
        temp_storage = set(map(int, input().split()))
        storage.symmetric_difference_update(temp_storage)
    elif operation[0] == 'difference_update':
        temp_storage = set(map(int, input().split()))
        storage.difference_update(temp_storage)
    else :
        assert False

print(sum(storage))

