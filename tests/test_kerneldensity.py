import cPickle, os
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from mpl_toolkits.basemap import Basemap

ff = os.path.join('.', 'test_data', 'kde_origin_lonLat.pck')
lonlat = cPickle.load(open(ff))

m1, m2 = lonlat.T
xmin = 70.0
xmax = 180.0
ymin = -36.
ymax = 0.

fig = plt.figure()
ax = fig.add_subplot(111)

# from StatInterface import KDEOrigin
# gridLimit={'xMin':70, 'xMax':180, 'yMin':-36, 'yMax':0}
# kdeStep = 0.1
# kdeOrigin = KDEOrigin.KDEOrigin(None, 'Gaussian', gridLimit, kdeStep, lonlat)
# x, y, z = kdeOrigin.generateKDE()
# ax.imshow(np.flipud(np.rot90(z)), cmap=plt.cm.gist_earth_r,
#           extent=[xmin, xmax, ymin, ymax])

X, Y = np.mgrid[xmin:xmax:10j, ymin:ymax:10j]
positions = np.vstack([X.ravel(), Y.ravel()])
values = np.vstack([m1, m2])
kernel = stats.gaussian_kde(values)
Z = np.reshape(kernel(positions).T, X.shape)

m = Basemap(projection='cyl', resolution='i', llcrnrlon=xmin, urcrnrlon=xmax, llcrnrlat=ymin, urcrnrlat=ymax)
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='#ffffff')
m.fillcontinents(color='#dedcd2',lake_color='#ffffff')
meridians = np.arange(xmin, xmax, 10.)
parallels = np.arange(ymin, ymax, 10.)
m.drawparallels(parallels, labels=[1,0,0,0], fontsize=9, linewidth=0.2)
m.drawmeridians(meridians, labels=[0,0,0,1], fontsize=9, linewidth=0.2)
plt.grid(True)


ax.imshow(np.rot90(Z), cmap=plt.cm.PuRd,
          extent=[xmin, xmax, ymin, ymax])


ax.plot(m1, m2, 'r.', markersize=2)
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
plt.show()
