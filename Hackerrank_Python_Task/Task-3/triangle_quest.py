# -*- coding: utf-8 -*-
"""Triangle Quest.ipynb"""

'''Task-  
You are given a positive integer N. Print a numerical triangle of height N - 1 like the one below:
1
22
333
4444
55555
Input Format :
A single line containing integer,N.

Output Format :
Print N -1 lines as explained above.
'''
for i in range(1,int(input())):   #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int(pow(10,i)//9)*i)
