# -*- coding: utf-8 -*-
"""Eye and Identity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DbB54zAq7SeUyv7POrtw_epoH1FWB1Ml
"""

import numpy

print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))

|