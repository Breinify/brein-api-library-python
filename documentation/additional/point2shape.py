from breinify import Breinify

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

apiKey = "938D-3120-64DD-413F-BB55-6573-90CE-473A"

lat = 28.5383
lon = -81.3792

brein = Breinify(apiKey)

result = brein.temporal_data(location_longitude=lon, location_latitude=lat, location_shapes = ["CITY","STATE"])

##note that there may be more than one set of coordinates (such as if there are holes or islands)
coords = result['location']['geojson']['STATE']['geometry']['coordinates'][1][0]

path = Path(coords)
fig = plt.figure()
ax = fig.add_subplot(111)
patch = patches.PathPatch(path, facecolor='green', lw=2)
ax.add_patch(patch)
ax.set_xlim(-90,-79)
ax.set_ylim(23,32)
plt.show()