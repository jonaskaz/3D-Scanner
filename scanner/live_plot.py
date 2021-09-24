import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

from config import DATA_FILEPATH


style.use("dark_background")
fig = plt.figure()
ax = plt.axes(projection="3d")


def animate(i):
    graph_data = open(DATA_FILEPATH, "r").read()
    lines = graph_data.split("\n")
    xs, ys, zs = [], [], []
    for line in lines:
        if len(line) > 1:
            x, y, z = line.split(",")
            xs.append(float(x))
            ys.append(float(y))
            zs.append(float(z))
    ax.clear()
    ax.scatter3D(xs, ys, zs, color="red")

# TODO label axes
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
