from awpy.data import NAV
from awpy.visualization.plot import plot_map, position_transform
from matplotlib.patches import Rectangle
from matplotlib.pyplot import show

f, ax = plot_map(map_name = "de_dust2", map_type = 'simpleradar',\
                 dark = True)

for a in NAV["de_dust2"]:
    area = NAV["de_dust2"][a]
    (area["southEastX"], area["northWestX"]),\
                    (area["southEastY"], area["northWestY"]) =\
            tuple(position_transform("de_dust2", b, "x") for b in\
                  (area["southEastX"], area["northWestX"])),\
            tuple(position_transform("de_dust2", b, "y") for b in\
                  (area["southEastY"], area["northWestY"]))
    width, height = area["southEastX"] - area["northWestX"],\
                    area["northWestY"] - area["southEastY"]
    southwest_x, southwest_y = area["northWestX"],\
                               area["southEastY"]
    rect = Rectangle((southwest_x,southwest_y), width, height,\
                     linewidth=1, edgecolor="yellow",\
                     facecolor="None")
    ax.add_patch(rect)

show()
