# -*- coding: utf-8 -*-
"""
  Name     : c1_14_read_pickle_data.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import pandas as pd
x=pd.read_pickle("c:/temp/ffMonthly.pkl")
print(x.head())