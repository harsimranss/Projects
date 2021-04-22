import os
import numpy as np
os.chdir('/home/sarhandi/stat')
a=np.load('data_set.npy',allow_pickle=True)
v1=np.load('velocity_data1.npy',allow_pickle=True)
v=np.load('velocity_data.npy',allow_pickle=True)
import matplotlib.pyplot as plt
plt.subplot(121)
plt.hist(v1,bins=np.arange(0,40,1))
plt.subplot(122)
plt.hist(v,bins=np.arange(0,40,1))
plt.title("final")
plt.show()
def update_coordinate(i, scatter):
    x, y, z = a[i]
    ax.clear()
    ax.set_xlim3d([-21,21])
    ax.set_ylim3d([-21,21])
    ax.set_zlim3d([-21,21])
    scatter[0]=ax.scatter3D(x,y,z,color='green')

import mpl_toolkits.mplot3d.axes3d as mp
import matplotlib.animation as animation

fig=plt.figure()
ax = plt.axes(projection ="3d")
ax.set_xlim3d([-21,21])
ax.set_ylim3d([-21,21])
ax.set_zlim3d([-21,21])
ax.set_title("Scatter Animation")
x,y,z=a[0]
scatter=[ax.scatter3D(x,y,z,color='green')]

anim=animation.FuncAnimation(fig,update_coordinate,len(a),fargs=(scatter,),interval=10)
plt.show()
