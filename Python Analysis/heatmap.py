'''
	Heatmap on first map
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

data_mrm = pd.read_csv('/home/cheng/BIgData/ItemOne/ItemOne-E-result.xls')
print ( data_mrm.shape )

data_mrm.drop_duplicates( inplace = True )

data_mrm.info

data = data_mrm.values
data_1 = [ i[0].split('\t') for i in data]
data_2 = [ list( map( float, i )  ) for i in data_1 ]
data_3 = np.array( data_2 )

data_erg = data_3*4096/800000
from scipy.ndimage.filters import gaussian_filter
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from scipy.misc.pilutil import imread

from scipy.ndimage.filters import gaussian_filter
import matplotlib.cm as cm
from matplotlib.colors import Normalize

def heatmap(x, y, s, bins=100):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins)
    heatmap = gaussian_filter(heatmap, sigma=s)

    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    return heatmap.T, extent


print(' ==== 1')
bg = imread('/home/cheng/BIgData/pubg-match-deaths/erangel.jpg')
hmap, extent = heatmap(data_erg[:,0], data_erg[:,1], s = 4.5 , bins = 200 )
alphas = np.clip(Normalize(0, hmap.max(), clip=True)(hmap)*4.5, 0.0, 1.)
colors = Normalize(0, hmap.max(), clip=True)(hmap)
colors = cm.Reds(colors)
colors[..., -1] = alphas

print(' ==== 2')

fig, ax = plt.subplots(figsize=(24,24))
ax.set_xlim(0, 4096); ax.set_ylim(0, 4096)
ax.imshow(bg)
ax.imshow(colors, extent=extent, origin='lower', cmap=cm.Reds, alpha=0.9)
plt.gca().invert_yaxis()

fig.savefig('plot.png')


'''
	Heatmap on second map 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

data_mrm = pd.read_csv('/home/cheng/BIgData/ItemOne/ItemOne-M-result.csv')
data_mrm.drop_duplicates( inplace = True )
data = data_mrm[ ['x','y' ] ].values
data = data * 1000 / 800000

from scipy.ndimage.filters import gaussian_filter
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from scipy.misc.pilutil import imread

def heatmap(x, y, s, bins=100):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins)
    heatmap = gaussian_filter(heatmap, sigma=s)

    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    return heatmap.T, extent

bg = imread('/home/cheng/BIgData/pubg-match-deaths/miramar.jpg')
hmap, extent = heatmap( data[:,0], data[:,1], 4 , bins = 200)
alphas = np.clip(Normalize(0, hmap.max(), clip=True)(hmap)*4, 0.0, 1.)
colors = Normalize(0, hmap.max(), clip=True)(hmap)
colors = cm.Reds(colors)
colors[..., -1] = alphas

fig, ax = plt.subplots(figsize=(24,24))
ax.set_xlim(0, 1000); ax.set_ylim(0, 1000)
ax.imshow(bg)
ax.imshow(colors, extent=extent, origin='lower', cmap=cm.Reds, alpha=1)
# plt.scatter( data[:,0], data[:,1])
plt.gca().invert_yaxis()
fig.savefig('plot_M.png')
