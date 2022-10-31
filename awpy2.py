from awpy.data import NAV
from awpy.visualization.plot import plot_map, position_transform
from matplotlib.patches import Rectangle
from awpy.analytics.nav import area_distance
from matplotlib.pyplot import show

f, ax = plot_map(map_name = "de_dust2", map_type = 'simpleradar',\
                 dark = True)

def getAreas():
    return area["northWestX"], area["southEastY"],\
           area["northWestY"], area["southEastX"]

nsAs, graph_dist = NAV["de_dust2"], area_distance(map_name =\
                                    "de_dust2", area_a = 152,\
                                    area_b = 8970,\
                                    dist_type = "graph")

for nA in nsAs:
    area = nsAs[nA]
    aNWX, aSEY, aNWY, aSEX = getAreas()
    (area["southEastX"], area["northWestX"]),\
                    (area["southEastY"], area["northWestY"]) =\
            tuple(position_transform("de_dust2", b, "x") for b in\
                  (aSEX, aNWX)),\
            tuple(position_transform("de_dust2", b, "y") for b in\
                  (aSEY, aNWY))
    color = "None"

    if nA in graph_dist["areas"]:
        color = "red"

    aNWX, aSEY, aNWY, aSEX = getAreas() 
    rect = Rectangle((aNWX, aSEY), aSEX - aNWX, aNWY - aSEY,\
        linewidth = 1, edgecolor = "yellow", facecolor = color)
    ax.add_patch(rect)

show()
