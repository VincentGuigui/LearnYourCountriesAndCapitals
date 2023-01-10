import geopandas
import matplotlib.pyplot as plt

import geopandas as gpd
import contextily as ctx
import rasterio
from rasterio.plot import show as rioshow
from shapely.geometry import box

folder = "cards"
plt.rcParams['figure.figsize'] = [10,10]
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# Load datas
world = geopandas.read_file("datas/ne_10m_admin_0_countries.shp")
cities = geopandas.read_file("datas/ne_110m_populated_places.shp")
# Load map base

# Keep only Capital cities 
cities = cities[cities["ADM0CAP"] == 1]

# Draw maps and cities locations
ax = cities.plot(ax=ax, marker='o', color='red', markersize=5)
# ax = world.plot(ax=ax, color='none', edgecolor='black', linewidth=0.5)
ctx.add_basemap(ax, crs=world.crs, source=ctx.providers.Stamen.TerrainBackground)

# Display the whole map
# minx, miny, maxx, maxy = world.total_bounds
# ax.set_xlim(minx, maxx)
# ax.set_ylim(miny, maxy)
# plt.show()
# exit()            

# For each country
for i in range(len(world)):
    country = world[world.NAME==world.NAME[i]]
    # Focus on the country
    minx, miny, maxx, maxy = world.bounds.loc[i]
    ax.set_xlim(minx, maxx)
    ax.set_ylim(miny, maxy)
    country.plot(ax=ax, color='none', edgecolor='black', linewidth=0.5)
    fig.savefig(folder + "/" + country.NAME[i] + "_1.png", bbox_inches='tight', pad_inches=0)
    
    # Add country name
    country_text = ax.text(country.LABEL_X[i], country.LABEL_Y[i], country.NAME[i], ha='center', color='darkgreen', size=35, fontweight="bold")
    fig.savefig(folder + "/" + country.NAME[i] + "_2_name.png", bbox_inches='tight', pad_inches=0)
    # Find capital cities (>=1 ?)
    capitals = cities.clip(country.geometry)
    city_texts = []
    for idx, capital in capitals.iterrows():
        # Add city name
        city_texts.append(ax.text(capitals.centroid[idx].x, capitals.centroid[idx].y, capital.NAME, ha='center', color='black', size=30, fontweight="bold"))        
    fig.savefig(folder + "/" + country.NAME[i] + "_3_capital.png", bbox_inches='tight', pad_inches=0)
    
    #Remove all labels
    country_text.remove()
    for city_text in city_texts:
        city_text.remove()
