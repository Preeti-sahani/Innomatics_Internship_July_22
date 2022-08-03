# -*- coding: utf-8 -*-
"""String Split and Join.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DbB54zAq7SeUyv7POrtw_epoH1FWB1Ml
"""

'''Task-  
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
Input Format
The one line contains a string consisting of space separated words. '''


def split_and_join(line):
    op = line.split();
    op = "-".join(op)
    return op

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
