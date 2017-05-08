# -*- coding: utf-8 -*-
'''
Created on 2017年3月6日

@author: didi
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a'],
'key2':['one', 'two', 'one', 'two', 'one'],
'data1':np.random.randn(5),
'data2':np.random.randn(5)})
print df
grouped = df['data1'].groupby([df['key1'],df['key2']])
print grouped.min()