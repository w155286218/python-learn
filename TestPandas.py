# -*- coding: utf-8 -*-
'''
Created on 2016-11-11

@author: Charlie
'''

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import chardet

reader = pd.read_csv('/Users/didi/Documents/dwd_vehicle_cyhz_slag_info.csv', sep='\t',iterator=False)
f=open('/Users/didi/Documents/pandas_test.txt','w')
print reader.groupby('dwd_vehicle_cyhz_slag_info.brand').count()
#print reader.head()
#f.write(str(reader.groupby('品牌'.decode('utf-8')).count()))
# try:
#     df = reader.get_chunk(100000)
# except StopIteration:
#     print "Iteration is stopped."
# for h in df.head():
#     print h
#     #print chardet.detect(h)

# df[0:3]
# df['didi_model_id']


# df = pd.DataFrame(np.random.randn(10, 4))
# print df.describe()

# df[0:3]
# df['didi_model_id']
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
#         'year': [2000, 2001, 2002, 2001, 2002],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# #DataFrame(data, columns=['year', 'state', 'pop'])
# frame = DataFrame(data)
# print frame
# print frame.T


#am_dw.dwd_vehicle_cyhz_slag_info.csv