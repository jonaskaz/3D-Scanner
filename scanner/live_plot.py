import matplotlib.pyplot as plt  #Import relevant libraries
import matplotlib.animation as animation
from matplotlib import style

#Import global variables, including file location for data from serial monitor and
#maximum acceptable x distance and minimum acceptable z distance
#(to eliminate data points representing the wall behind the letter and floor below).
from config import DATA_FILEPATH, MAX_X_DISTANCE, MIN_Z_DISTANCE

#Defining 3D plot space
style.use("dark_background")
fig = plt.figure()
ax = plt.axes(projection="3d")

def animate(i):
    graph_data = open(DATA_FILEPATH, "r").read()
    lines = graph_data.split("\n")
    xs, ys, zs = [], [], []  #Sorting data to be read and plotted
    for line in lines:
        if len(line) > 1:
            x, y, z = line.split(",")
            if float(x) > MAX_X_DISTANCE:  #if statements to check if point is within acceptable distance range
                continue
            elif float(z) < MIN_Z_DISTANCE:
                continue
            xs.append(float(x))
            ys.append(float(y))
            zs.append(float(z))
    ax.clear()
    ax.set_label("3D IR Scan")  #Labeling plot and axes
    ax.set_xlabel("X (cm)")
    ax.set_ylabel("Y (cm)")
    ax.set_zlabel("Z (cm)")
    ax.scatter3D(xs, ys, zs, color="blue")
    
#Plotting points representing letter as distance values are read from text file
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
