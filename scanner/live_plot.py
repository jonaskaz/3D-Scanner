import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

from config import DATA_FILEPATH, MAX_X_DISTANCE, MIN_Z_DISTANCE


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
            if float(x) > MAX_X_DISTANCE:
                continue
            elif float(z) < MIN_Z_DISTANCE:
                continue
            xs.append(float(x))
            ys.append(float(y))
            zs.append(float(z))
    ax.clear()
    ax.set_label("3D IR Scan")
    ax.set_xlabel("X (cm)")
    ax.set_ylabel("Y (cm)")
    ax.set_zlabel("Z (cm)")
    ax.scatter3D(xs, ys, zs, color="blue")
    

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
