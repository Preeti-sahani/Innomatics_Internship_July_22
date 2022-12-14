# -*- coding: utf-8 -*-
"""No Idea.ipynb"""

'''Task- 
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
You like all the integers in set A and dislike all the integers in set B. 
Your initial happiness is o. For each i integer in the array, if i belons to A, you add 1 to your happiness. 
If i belong to B, you add -1 to your happiness. Otherwise, your happiness does not change. 
Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.
Constraints:
   1.    1<=n<=10^5
   2.    1<=m<=10^5
   3.    1<=any integer in the input <=10^9
Input Format:
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.y'''

n, m = map(int,input().split())
arr = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))

print(sum((i in A) -(i in B) for i in arr))
