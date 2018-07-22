import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
%matplotlib inline

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv('./data/aa')

data.head

data.columns = ['match' , 'dist' , 'place']
# data.drop_duplicates( inplace = True )

print( data.head )


data['won'] = data['place'] == 1
data['person'] = 1
print( data.head  )

data['drove'] = data['dist'] != 0

dist_ride = data.loc[data['dist']<12000, ['dist', 'won', 'person']]
labels=["0-1k", "1-2k", "2-3k", "3-4k","4-5k", "5-6k", "6-7k", "7-8k", "8-9k", "9-10k", "10-11k", "11-12k"]
dist_ride['drove_cut'] = pd.cut(dist_ride['dist'], 12, labels=labels)
target = dist_ride.groupby('drove_cut').sum()

import os

for i in os.walk('data'):
    for j in i :
        if type( j ) == list and len(j) > 0:
            for k in j :
                if k == 'aa' or k == 'bk' or k == 'an' or k == 'bb' or k == 'bl' or k == 'bx':
                    continue
                tmp = './data/' + k 
                print( tmp )
                tmp = pd.read_csv( tmp )
                tmp.columns = ['match' , 'dist' , 'place']
                
                tmp['won'] = tmp['place'] == 1
                tmp['person'] = 1
                tmp = tmp[ tmp.dist.apply(lambda x: (type(x) in [float]) or (x.isnumeric()) )]
                tmp['drove'] = tmp['dist'] != 0
                
                dist_ride = tmp.loc[ tmp['dist']<12000, ['dist', 'won', 'person'] ]
#                 labels=["0-1k", "1-2k", "2-3k", "3-4k","4-5k", "5-6k", "6-7k", "7-8k", "8-9k", "9-10k", "10-11k", "11-12k"]
                dist_ride['drove_cut'] = pd.cut(dist_ride['dist'], 12, labels=labels)
                tmp_target = dist_ride.groupby('drove_cut').sum()
        
                target = target + tmp_target
            
                print( target )

target.to_csv( './result/result.csv')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
%matplotlib inline

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

target = pd.read_csv( './result/result.csv')

target.head

target['ratio'] = target.won / target.person

print( target.head )

new_target = target[ ['drove_cut', 'ratio'] ]

print( new_target.head )

dist_ride = new_target

dist_ride.head

my_colors = 'rgbkymc'

dist_ride.groupby('drove_cut' , sort = False ).ratio.sum().plot.bar(figsize=(8, 4) , color=my_colors, rot = 60, stacked=True )
plt.xlabel("搭乘车辆里程", fontsize=14)
plt.ylabel("吃鸡概率", fontsize=14)
plt.title('搭乘车辆里程与吃鸡概率的关系', fontsize=14)
