# -*- coding: utf-8 -*-
"""Concatenate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DbB54zAq7SeUyv7POrtw_epoH1FWB1Ml
"""

import numpy as np
a, b, c = map(int,input().split())
arrA = np.array([input().split() for _ in range(a)],int)
arrB = np.array([input().split() for _ in range(b)],int)
print(np.concatenate((arrA, arrB), axis = 0))

|