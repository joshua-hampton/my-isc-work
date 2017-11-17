#!/usr/bin/python

import matplotlib.pyplot as plt
from example_data.map_data import *
from mpl_toolkits.basemap import Basemap

fig=plt.figure()
m=Basemap(projection='cyl',llcrnrlat=-90, urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180,resolution='c')
m.drawcoastlines()
im1=m.pcolormesh(lons,lats,tas,shading='flat',cmap=plt.cm.jet,latlon=True)
plt.savefig('tas1.png')

plt.title('Change in sfc air temp from MOHC HadGEM2-ES')
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))
cb=m.colorbar(im1,'bottom',size='5%',pad='2%')
plt.savefig('tas2.png')
plt.show()
plt.close()
