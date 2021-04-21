import numpy as np 
from numpy import random as rd

class particle():

    objects = []

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.accelatation = (0, 0, 0)
        self.neighbours = []
        particle.objects.append(self)

    @classmethod
    def update(cls):
        for obj in cls.objects:
            x, y, z = obj.position
            vx, vy, vz = obj.velocity
            
            if x>10:
                obj.velocity=(-abs(obj.velocity[0]),obj.velocity[1],obj.velocity[2])
            if y>10:
                obj.velocity=(obj.velocity[0],-abs(obj.velocity[1]),obj.velocity[2])
            if z>10:
                obj.velocity=(obj.velocity[0],obj.velocity[1],-abs(obj.velocity[2]))
            if x<-10:
                obj.velocity=(abs(obj.velocity[0]),obj.velocity[1],obj.velocity[2])
            if y<-10:
                obj.velocity=(obj.velocity[0],abs(obj.velocity[1]),obj.velocity[2])
            if z<-10:
                obj.velocity=(obj.velocity[0],obj.velocity[1],abs(obj.velocity[2]))
          

            vx, vy, vz = obj.velocity
            ax, ay, az = obj.accelatation
            obj.accelatation = obj.force()
            obj.position = (x + 0.1 * vx, y + 0.1 * vy, z + 0.1 * vz)
            obj.velocity = (vx + obj.accelatation[0] * 0.1, vy + obj.accelatation[1] * 0.1, vz + obj.accelatation[2] * 0.1)

    def force(self):
        f = (0, 0, 0)
        x0, y0, z0 = self.position
        for obj in particle.objects:
            x, y, z = obj.position
            if self.position != obj.position:
                f = (f[0] + 1/(x - x0), f[1] + 1/(y - y0), f[2] +1/(z - z0))
        return f
            

    @classmethod
    def energy(cls):
        e = 0
        for obj in cls.objects:
            vx, vy, vz = obj.velocity
            e = e + vx**2 + vy**2 + vz**2
        return('Energy: ', e)

    x_list = []
    y_list = []
    z_list = []

    @classmethod
    def getcoordinate(cls):
        cls.x_list = []
        cls.y_list = []
        cls.z_list = []

        for obj in cls.objects:
            x, y, z = obj.position
            cls.x_list.append(x)
            cls.y_list.append(y)
            cls.z_list.append(z)
        return cls.x_list, cls.y_list, cls.z_list
###########################################################
######### CLASS SAMPANN HOI ###############################

def create():
    lists = []
    for i in range(5):
        x = 10 * rd.random()
        y = 10 * rd.random()
        z = 10 * rd.random()
        vx = rd.random()
        vy = rd.random()
        vz = rd.random()
        
        lists.append(particle((x, y, z), (vx, vy, vz)))

def update_coordinate(i, scatter):
    particle.update()
    x, y, z = particle.getcoordinate()
    ax.clear()
    ax.set_xlim3d([-11,11])
    ax.set_ylim3d([-11,11])
    ax.set_zlim3d([-11,11])
    scatter[0]=ax.scatter3D(x,y,z,color='green')

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as mp
import matplotlib.animation as animation
print(particle.energy())
create()
print(particle.energy())
fig=plt.figure()
ax = plt.axes(projection ="3d")
ax.set_xlim3d([0,5])
ax.set_ylim3d([0,5])
ax.set_zlim3d([0,5])
ax.set_title("Scatter Animation")
x,y,z=particle.getcoordinate()
scatter=[ax.scatter3D(x,y,z,color='green')]

anim=animation.FuncAnimation(fig,update_coordinate,40,fargs=(scatter,),interval=50)
plt.show()


