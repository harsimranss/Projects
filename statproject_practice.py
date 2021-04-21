import numpy as np 
from numpy import random as rd
import time
timestart=time.process_time()
class particle():

    objects = []
    time=0
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.accelaration = (0, 0, 0)
        self.neighbours = []
        particle.objects.append(self)

    @classmethod
    def update(cls):
        t=0.01
        # updating neighbours
        if particle.time%5==0:
            particle.update_neighbours()
        # updating accelaration before updating coordinates
        particle.update_ac()
        for obj in cls.objects:
            x, y, z = obj.position
            vx, vy, vz = obj.velocity
            
            if x>20:
                obj.velocity=(-abs(obj.velocity[0]),obj.velocity[1],obj.velocity[2])
            if y>20:
                obj.velocity=(obj.velocity[0],-abs(obj.velocity[1]),obj.velocity[2])
            if z>20:
                obj.velocity=(obj.velocity[0],obj.velocity[1],-abs(obj.velocity[2]))
            if x<-20:
                obj.velocity=(abs(obj.velocity[0]),obj.velocity[1],obj.velocity[2])
            if y<-20:
                obj.velocity=(obj.velocity[0],abs(obj.velocity[1]),obj.velocity[2])
            if z<-20:
                obj.velocity=(obj.velocity[0],obj.velocity[1],abs(obj.velocity[2]))
          

            vx, vy, vz = obj.velocity
            ax, ay, az = obj.accelaration
            #removing
            'obj.accelatation = obj.force()'
            obj.position = (x + t * vx, y + t * vy, z + t * vz)
            vx=vx + obj.accelaration[0] * t
            vy=vy + obj.accelaration[1] * t
            vz=vz+obj.accelaration[2] * t
            obj.velocity = (vx,vy,vz)
            particle.time=particle.time+1
    def force(self):
        f = (0, 0, 0)
        R = 1 # boundary of neighbourhood
        x0, y0, z0 = self.position
        for obj in self.neighbours:
            x, y, z = obj.position
            r=((x-x0)**2+(y-y0)**2 +(z-z0)**2)**(1.5)
            f = (f[0] -1*(x-x0)/r, f[1] -1*(y - y0)/r, f[2] - 1*(z - z0)/r)
        # changing accelaration so as to not calculate force for future config.
        self.accelaration=f

    @classmethod
    def update_neighbours(cls):
        R_critical=2
        for obj in cls.objects:
            for obj2 in cls.objects:
                x,y,z=obj.position
                x1,y1,z1=obj2.position
                r=((x-x1)**2+(y-y1)**2+(z-z1)**2)**0.5
                if r<R_critical and r>0:
                    obj.neighbours.append(obj2)

    @classmethod
    def energy(cls):
        e = 0
        for obj in cls.objects:
            vx, vy, vz = obj.velocity
            e = e + vx**2 + vy**2 + vz**2
        return('Energy: ', e)
    # creating function to update acceleration
    @classmethod
    def update_ac(cls):
        for obj in cls.objects:
            obj.force()
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
    @classmethod
    def velocity_distribution(cls):
        v=[]
        for obj in cls.objects:
            v.append((obj.velocity[0]**2+obj.velocity[1]**2+obj.velocity[2]**2)**0.5)
        np.save('velocity_data.npy',v,allow_pickle=True)
    @classmethod
    def velocity_distribution1(cls):
        v1=[]
        for obj in cls.objects:
            v1.append((obj.velocity[0]**2+obj.velocity[1]**2+obj.velocity[2]**2)**0.5)
        np.save('velocity_data1.npy',v1,allow_pickle=True)
###########################################################
######### CLASS SAMPANN HOI ###############################

def create():
    lists = []
    for i in range(1000):
        x = 0.02*rd.randint(-1000,1000)
        y = 0.02*rd.randint(-1000,1000)
        z = 0.02*rd.randint(-1000,1000)
        vx = 0.1*rd.randint(-100,100)
        vy = 0.1*rd.randint(-100,100)
        vz = 0.1*rd.randint(-100,100)
        
        lists.append(particle((x, y, z), (vx, vy, vz)))
create()
data_set=[]
print('Working On it!!')
import os
os.chdir('/home/sarhandi/stat')
particle.velocity_distribution1()
for pp in range(1000):
	particle.update()
	data_set.append(particle.getcoordinate())
print('Wait is Over!!!!')
timeend=time.process_time()
print('Total time taken:',timeend-timestart)



particle.velocity_distribution()
np.save('data_set.npy',data_set,allow_pickle=True)
print('donee!! step 1')
print('Animation begins')
'''def update_coordinate(i, scatter):
    particle.update()
    x, y, z = particle.getcoordinate()
    ax.clear()
    ax.set_xlim3d([-21,21])
    ax.set_ylim3d([-21,21])
    ax.set_zlim3d([-21,21])
    scatter[0]=ax.scatter3D(x,y,z,color='green')

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as mp
import matplotlib.animation as animation
print(particle.energy())
create()
particle.velocity_distribution()
print(particle.energy())
fig=plt.figure()
ax = plt.axes(projection ="3d")
ax.set_xlim3d([-21,21])
ax.set_ylim3d([-21,21])
ax.set_zlim3d([-21,21])
ax.set_title("Scatter Animation")
x,y,z=particle.getcoordinate()
scatter=[ax.scatter3D(x,y,z,color='green')]

anim=animation.FuncAnimation(fig,update_coordinate,40,fargs=(scatter,),interval=50)
plt.show()'''


