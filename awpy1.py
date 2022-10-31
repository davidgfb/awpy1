from awpy.data import NAV
from awpy.visualization.plot import plot_map, position_transform
from matplotlib.patches import Rectangle
from matplotlib.pyplot import show

f, ax = plot_map(map_name = "de_dust2", map_type = 'simpleradar',\
                 dark = True)

def getAreas():
    return area["northWestX"], area["southEastY"],\
           area["northWestY"], area["southEastX"]

nsAs = NAV["de_dust2"]

for nA in nsAs:
    area = nsAs[nA]
    aNWX, aSEY, aNWY, aSEX = getAreas()
    (area["southEastX"], area["northWestX"]),\
                    (area["southEastY"], area["northWestY"]) =\
            tuple(position_transform("de_dust2", b, "x") for b in\
                  (aSEX, aNWX)),\
            tuple(position_transform("de_dust2", b, "y") for b in\
                  (aSEY, aNWY))                     
    aNWX, aSEY, aNWY, aSEX = getAreas()
    rect = Rectangle((aNWX, aSEY), aSEX - aNWX,\
                     aNWY - aSEY, linewidth = 1,\
                     edgecolor = "yellow", facecolor = "None")
    ax.add_patch(rect)

show()
