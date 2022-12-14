from awpy.data import NAV
from awpy.visualization.plot import plot_map, position_transform
from matplotlib.patches import Rectangle
from awpy.analytics.nav import area_distance
from matplotlib.pyplot import show

nM = 'de_dust2'
geodesic_dist, (f, ax), nsAs = area_distance(\
    map_name = nM, area_a = 152, area_b = 8970,\
    dist_type = "geodesic"), plot_map(map_name = nM,\
    map_type = 'simpleradar', dark = True), NAV[nM]

def getAreas():
    return area["northWestX"], area["southEastY"],\
           area["northWestY"], area["southEastX"]

for nA in nsAs:
    area = nsAs[nA]
    aNWX, aSEY, aNWY, aSEX = getAreas()
    (area["southEastX"], area["northWestX"]),\
                    (area["southEastY"], area["northWestY"]) =\
            tuple(position_transform(nM, b, "x") for b in\
                  (aSEX, aNWX)),\
            tuple(position_transform(nM, b, "y") for b in\
                  (aSEY, aNWY))
    color = "None"

    if nA in geodesic_dist["areas"]:
        color = "red"

    aNWX, aSEY, aNWY, aSEX = getAreas()
    rect = Rectangle((aNWX, aSEY), aSEX - aNWX, aNWY - aSEY,\
                     linewidth = 1, edgecolor = "yellow",\
                     facecolor = color)
    ax.add_patch(rect)

show()
