'''
	Draw circle on fist map
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import OrderedDict
%matplotlib inline

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

pth = '/home/cheng/BIgData/K_means/E-kmeans/'
fst = 'E-kmeansResult_0.csv'

original_data = pd.read_csv( pth + fst )

original_data.columns = ['class' , 'x', 'y']

print( original_data.head )

import os

for _, _, i  in os.walk(pth):
    for j in sorted( i ):
        if j == fst :
            continue
            
        print( pth + j )
        tmp_data = pd.read_csv( pth + j )
        tmp_data.columns = ['class', 'x' , 'y']
        
        original_data = original_data.append( tmp_data )
        
        print( original_data.head )

original_data.columns = ['c','x','y']

original_data.to_csv('original.csv')

cFst = original_data.loc[ original_data['c'] == 1]
cScd = original_data.loc[ original_data['c'] == 2]
cTrd = original_data.loc[ original_data['c'] == 3]
cFth = original_data.loc[ original_data['c'] == 4]

cFst_ = cFst[ ['x','y'] ]
cScd_ = cScd[ ['x','y'] ]
cTrd_ = cTrd[ ['x','y'] ]
cFth_ = cFth[ ['x','y'] ]

cFst_v = cFst_.values*4096/800000
cScd_v = cScd_.values*4096/800000
cTrd_v = cTrd_.values*4096/800000
cFth_v = cFth_.values*4096/800000

def calculate_circle(data):

    dic = dict()
    for ( x , y ) in data:
        
        if x not in dic:
            dic[x] = [y , y ]
        if y < dic[x][0]:
            dic[x][0] = y
        elif y > dic[x][1]:
            dic[x][1] = y
            
    dic = OrderedDict(sorted(dic.items()))
    k = np.array( list( dic.keys()  ) )
    v = np.array( list( dic.values()) )

    length = v.shape[0]
    for i in range( 1 , length -1 ):
        if v[i][0] == v[i][1]:
            v[i][0] = min( v[i][0] , (v[i-1][0] + v[i+1][0] ) / 2 )
            v[i][1] = max( v[i][1] , (v[i-1][1] + v[i+1][1] ) / 2 )

    upper_bound = np.vstack( ( k , v[:,0])).transpose()
    lower_bound = np.vstack( ( k , v[:,1])).transpose()

    print( upper_bound )
    print( lower_bound )
    return upper_bound, lower_bound
fst_upper_bound, fst_lower_bound = calculate_circle( cFst_v )
scd_upper_bound, scd_lower_bound = calculate_circle( cScd_v )
trd_upper_bound, trd_lower_bound = calculate_circle( cTrd_v )
fth_upper_bound, fth_lower_bound = calculate_circle( cFth_v )

fst_upper_bound_, fst_lower_bound_ = fst_upper_bound.copy() , fst_lower_bound.copy()
scd_upper_bound_, scd_lower_bound_ = scd_upper_bound.copy() , scd_lower_bound.copy()
trd_upper_bound_, trd_lower_bound_ = trd_upper_bound.copy() , trd_lower_bound.copy()
fth_upper_bound_, fth_lower_bound_ = fth_upper_bound.copy() , fth_lower_bound.copy(

	fst_upper_bound, fst_lower_bound = fst_upper_bound_.copy() , fst_lower_bound_.copy()
scd_upper_bound, scd_lower_bound = scd_upper_bound_.copy() , scd_lower_bound_.copy()
trd_upper_bound, trd_lower_bound = trd_upper_bound_.copy() , trd_lower_bound_.copy()
fth_upper_bound, fth_lower_bound = fth_upper_bound_.copy() , fth_lower_bound_.copy()

def discrete( data , bins = 10 ):
    low_value = data[0,0]
    up_value = data[-1,0]
    
    gap = ( up_value - low_value ) / bins
    
    cnt = 0
    lst = []
    
    for i in data:
        target = low_value + gap * cnt
        if i[0] >= target:
            lst.append( i )
            cnt = cnt + 1
    return np.array( lst )
tst = discrete( fst_upper_bound )
print( tst )

mybin = 5
my_line = 7.0

fst_upper_bound, fst_lower_bound = fst_upper_bound_.copy() , fst_lower_bound_.copy()
scd_upper_bound, scd_lower_bound = scd_upper_bound_.copy() , scd_lower_bound_.copy()
trd_upper_bound, trd_lower_bound = trd_upper_bound_.copy() , trd_lower_bound_.copy()
fth_upper_bound, fth_lower_bound = fth_upper_bound_.copy() , fth_lower_bound_.copy()

fst_upper_bound = discrete( fst_upper_bound, bins = mybin ) 
fst_lower_bound = discrete( fst_lower_bound, bins = mybin )
scd_upper_bound = discrete( scd_upper_bound, bins = mybin )
scd_lower_bound = discrete( scd_lower_bound, bins = mybin )
trd_upper_bound = discrete( trd_upper_bound, bins = mybin )
trd_lower_bound = discrete( trd_lower_bound, bins = mybin )
fth_upper_bound = discrete( fth_upper_bound, bins = mybin )
fth_lower_bound = discrete( fth_lower_bound, bins = mybin )

from scipy.ndimage.filters import gaussian_filter
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from scipy.misc.pilutil import imread
from scipy.ndimage.filters import gaussian_filter
import matplotlib.cm as cm
from matplotlib.colors import Normalize


bg = imread('/home/cheng/BIgData/pubg-match-deaths/erangel.jpg')
fig, ax = plt.subplots(figsize=(24,24))
ax.set_xlim(0, 4096); ax.set_ylim(0, 4096)
ax.imshow(bg)
# ax.imshow(colors, extent=extent, origin='lower', cmap=cm.Reds, alpha=0.9)

ax.plot( fst_upper_bound[:,0], fst_upper_bound[:,1] , 'r-', linewidth = my_line)
ax.plot( fst_lower_bound[:,0], fst_lower_bound[:,1] , 'r-', linewidth = my_line)
ax.plot( [ fst_upper_bound[0,0], fst_lower_bound[0,0] ], [ fst_upper_bound[0,1], fst_lower_bound[0,1] ] )
ax.plot( [ fst_upper_bound[-1,0], fst_lower_bound[-1,0] ], [ fst_upper_bound[-1,1], fst_lower_bound[-1,1] ] )

ax.plot( scd_upper_bound[:,0], scd_upper_bound[:,1] , 'y-', linewidth = my_line )
ax.plot( scd_lower_bound[:,0], scd_lower_bound[:,1] , 'y-', linewidth = my_line )
ax.plot( [ scd_upper_bound[0,0], scd_lower_bound[0,0] ], [ scd_upper_bound[0,1], scd_lower_bound[0,1] ] )
ax.plot( [ scd_upper_bound[-1,0], scd_lower_bound[-1,0] ], [ scd_upper_bound[-1,1], scd_lower_bound[-1,1] ] )

ax.plot( trd_upper_bound[:,0], trd_upper_bound[:,1] , 'b-', linewidth = my_line)
ax.plot( trd_lower_bound[:,0], trd_lower_bound[:,1] , 'b-', linewidth = my_line)
ax.plot( [ trd_upper_bound[0,0], trd_lower_bound[0,0] ], [ trd_upper_bound[0,1], trd_lower_bound[0,1] ] )
ax.plot( [ trd_upper_bound[-1,0], trd_lower_bound[-1,0] ], [ trd_upper_bound[-1,1], trd_lower_bound[-1,1] ] )

ax.plot( fth_upper_bound[:,0], fth_upper_bound[:,1] , 'w-', linewidth = my_line)
ax.plot( fth_lower_bound[:,0], fth_lower_bound[:,1] , 'w-', linewidth = my_line )
ax.plot( [ fth_upper_bound[0,0], fth_lower_bound[0,0] ], [ fth_upper_bound[0,1], fth_lower_bound[0,1] ] )
ax.plot( [ fth_upper_bound[-1,0], fth_lower_bound[-1,0] ], [ fth_upper_bound[-1,1], fth_lower_bound[-1,1] ] )     

plt.gca().invert_yaxis()

fig.savefig('plot_E_circle.png')



'''
	Draw circle on second map
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import OrderedDict
%matplotlib inline

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

pth = '/home/cheng/BIgData/K_means/M-kmeans/'
fst = 'M-kmeans_0.csv'

original_data = pd.read_csv( pth + fst )

original_data.columns = ['class' , 'x', 'y']

print( original_data.head )

import os

for _, _, i  in os.walk(pth):
    for j in sorted( i ):
        if j == fst :
            continue
            
        print( pth + j )
        tmp_data = pd.read_csv( pth + j )
        tmp_data.columns = ['class', 'x' , 'y']
        
        original_data = original_data.append( tmp_data )
        
        print( original_data.head )

original_data.columns = ['c','x','y']
original_data.to_csv('original_.csv')

cFst = original_data.loc[ original_data['c'] == 1]
cScd = original_data.loc[ original_data['c'] == 2]
cTrd = original_data.loc[ original_data['c'] == 3]
cFth = original_data.loc[ original_data['c'] == 4]

cFst_ = cFst[ ['x','y'] ]
cScd_ = cScd[ ['x','y'] ]
cTrd_ = cTrd[ ['x','y'] ]
cFth_ = cFth[ ['x','y'] ]

cFst_v = cFst_.values*1000/800000
cScd_v = cScd_.values*1000/800000
cTrd_v = cTrd_.values*1000/800000
cFth_v = cFth_.values*1000/800000

def calculate_circle(data):

    dic = dict()
    for ( x , y ) in data:
        
        if x not in dic:
            dic[x] = [y , y ]
        if y < dic[x][0]:
            dic[x][0] = y
        elif y > dic[x][1]:
            dic[x][1] = y
            
    dic = OrderedDict(sorted(dic.items()))
    k = np.array( list( dic.keys()  ) )
    v = np.array( list( dic.values()) )

    length = v.shape[0]
    for i in range( 1 , length -1 ):
        if v[i][0] == v[i][1]:
            v[i][0] = min( v[i][0] , (v[i-1][0] + v[i+1][0] ) / 2 )
            v[i][1] = max( v[i][1] , (v[i-1][1] + v[i+1][1] ) / 2 )

    upper_bound = np.vstack( ( k , v[:,0])).transpose()
    lower_bound = np.vstack( ( k , v[:,1])).transpose()

    print( upper_bound )
    print( lower_bound )
    return upper_bound, lower_bound

fst_upper_bound, fst_lower_bound = calculate_circle( cFst_v )
scd_upper_bound, scd_lower_bound = calculate_circle( cScd_v )
trd_upper_bound, trd_lower_bound = calculate_circle( cTrd_v )
fth_upper_bound, fth_lower_bound = calculate_circle( cFth_v )

fst_upper_bound_, fst_lower_bound_ = fst_upper_bound.copy() , fst_lower_bound.copy()
scd_upper_bound_, scd_lower_bound_ = scd_upper_bound.copy() , scd_lower_bound.copy()
trd_upper_bound_, trd_lower_bound_ = trd_upper_bound.copy() , trd_lower_bound.copy()
fth_upper_bound_, fth_lower_bound_ = fth_upper_bound.copy() , fth_lower_bound.copy()

fst_upper_bound, fst_lower_bound = fst_upper_bound_.copy() , fst_lower_bound_.copy()
scd_upper_bound, scd_lower_bound = scd_upper_bound_.copy() , scd_lower_bound_.copy()
trd_upper_bound, trd_lower_bound = trd_upper_bound_.copy() , trd_lower_bound_.copy()
fth_upper_bound, fth_lower_bound = fth_upper_bound_.copy() , fth_lower_bound_.copy()

def discrete( data , bins = 10 ):
    low_value = data[0,0]
    up_value = data[-1,0]
    
    gap = ( up_value - low_value ) / bins
    
    cnt = 0
    lst = []
    
    for i in data:
        target = low_value + gap * cnt
        if i[0] >= target:
            lst.append( i )
            cnt = cnt + 1
    return np.array( lst )

mybin = 7
my_line = 6.0

fst_upper_bound, fst_lower_bound = fst_upper_bound_.copy() , fst_lower_bound_.copy()
scd_upper_bound, scd_lower_bound = scd_upper_bound_.copy() , scd_lower_bound_.copy()
trd_upper_bound, trd_lower_bound = trd_upper_bound_.copy() , trd_lower_bound_.copy()
fth_upper_bound, fth_lower_bound = fth_upper_bound_.copy() , fth_lower_bound_.copy()

fst_upper_bound = discrete( fst_upper_bound, bins = mybin ) 
fst_lower_bound = discrete( fst_lower_bound, bins = mybin )
scd_upper_bound = discrete( scd_upper_bound, bins = 5 )
scd_lower_bound = discrete( scd_lower_bound, bins = 5 )
trd_upper_bound = discrete( trd_upper_bound, bins = 5 )
trd_lower_bound = discrete( trd_lower_bound, bins = 4 )
fth_upper_bound = discrete( fth_upper_bound, bins = 5 )
fth_lower_bound = discrete( fth_lower_bound, bins = 5 )

from scipy.ndimage.filters import gaussian_filter
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from scipy.misc.pilutil import imread
from scipy.ndimage.filters import gaussian_filter
import matplotlib.cm as cm
from matplotlib.colors import Normalize

bg = imread('/home/cheng/BIgData/pubg-match-deaths/miramar.jpg')
fig, ax = plt.subplots(figsize=(24,24))
ax.set_xlim(0, 1000); ax.set_ylim(0, 1000)
ax.imshow(bg)
# ax.imshow(colors, extent=extent, origin='lower', cmap=cm.Reds, alpha=0.9)

ax.plot( fst_upper_bound[:,0], fst_upper_bound[:,1] , 'r-', linewidth = my_line)
ax.plot( fst_lower_bound[:,0], fst_lower_bound[:,1] , 'r-', linewidth = my_line)
ax.plot( [ fst_upper_bound[0,0], fst_lower_bound[0,0] ], [ fst_upper_bound[0,1], fst_lower_bound[0,1] ] )
ax.plot( [ fst_upper_bound[-1,0], fst_lower_bound[-1,0] ], [ fst_upper_bound[-1,1], fst_lower_bound[-1,1] ] )

ax.plot( scd_upper_bound[:,0], scd_upper_bound[:,1] , 'y-', linewidth = my_line )
ax.plot( scd_lower_bound[:,0], scd_lower_bound[:,1] , 'y-', linewidth = my_line )
ax.plot( [ scd_upper_bound[0,0], scd_lower_bound[0,0] ], [ scd_upper_bound[0,1], scd_lower_bound[0,1] ] )
ax.plot( [ scd_upper_bound[-1,0], scd_lower_bound[-1,0] ], [ scd_upper_bound[-1,1], scd_lower_bound[-1,1] ] )

ax.plot( trd_upper_bound[:,0], trd_upper_bound[:,1] , 'b-', linewidth = my_line)
ax.plot( trd_lower_bound[:,0], trd_lower_bound[:,1] , 'b-', linewidth = my_line)
ax.plot( [ trd_upper_bound[0,0], trd_lower_bound[0,0] ], [ trd_upper_bound[0,1], trd_lower_bound[0,1] ] )
ax.plot( [ trd_upper_bound[-1,0], trd_lower_bound[-1,0] ], [ trd_upper_bound[-1,1], trd_lower_bound[-1,1] ] )

ax.plot( fth_upper_bound[:,0], fth_upper_bound[:,1] , 'w-', linewidth = my_line)
ax.plot( fth_lower_bound[:,0], fth_lower_bound[:,1] , 'w-', linewidth = my_line )
ax.plot( [ fth_upper_bound[0,0], fth_lower_bound[0,0] ], [ fth_upper_bound[0,1], fth_lower_bound[0,1] ] )
ax.plot( [ fth_upper_bound[-1,0], fth_lower_bound[-1,0] ], [ fth_upper_bound[-1,1], fth_lower_bound[-1,1] ] )     

plt.gca().invert_yaxis()

fig.savefig('plot_M_circle.png')

