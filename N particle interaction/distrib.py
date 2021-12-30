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
        t=0.1
        # updating accelaration before updating coordinates
        particle.update_ac()
        for obj in cls.objects:
            x, y, z = obj.position
            vx, vy, vz = obj.velocity
            
            if x>6:
                obj.velocity=(-abs(obj.velocity[0]),obj.velocity[1],obj.velocity[2])
            if y>6:
                obj.velocity=(obj.velocity[0],-abs(obj.velocity[1]),obj.velocity[2])
            if z>6:
                obj.velocity=(obj.velocity[0],obj.velocity[1],-abs(obj.velocity[2]))
            if x<-6:
                obj.velocity=(abs(obj.velocity[0]),obj.velocity[1],obj.velocity[2])
            if y<-6:
                obj.velocity=(obj.velocity[0],abs(obj.velocity[1]),obj.velocity[2])
            if z<-6:
                obj.velocity=(obj.velocity[0],obj.velocity[1],abs(obj.velocity[2]))
          

            vx, vy, vz = obj.velocity
            ax, ay, az = obj.accelatation
            #removing
            'obj.accelatation = obj.force()'
            obj.position = (x + t * vx, y + t * vy, z + t * vz)
            obj.velocity = (vx + obj.accelatation[0] * t, vy + obj.accelatation[1] * t, vz + obj.accelatation[2] * t)

    def force(self):
        f = (0, 0, 0)
        x0, y0, z0 = self.position
        for obj in particle.objects:
            x, y, z = obj.position
            if self.position != obj.position:
                r=((x-x0)**2+(y-y0)**2 +(z-z0)**2)**(1.5)
                f = (f[0] +10*(x-x0)/r, f[1] +10*(y - y0)/r, f[2] + 10*(z - z0)/r)
        # changing accelaration so as to not calculate force for future config.
        self.accelaration=f

    @classmethod
    def velocity_distribution(cls):
        v=[]
        for obj in cls.objects:
            v.append(obj.velocity[0]**2+obj.velocity[1]**2+obj.velocity[2]**2)
        import matplotlib.pyplot as plt
        plt.hist(v,bins=np.arange(0,3,0.1))
        plt.show()

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
###########################################################
######### CLASS SAMPANN HOI ###############################

def create():
    lists = []
    for i in range(150):
        x =  0.005*rd.randint(-1000,1000)
        y = 0.005*rd.randint(-1000,1000)
        z = 0.005*rd.randint(-1000,1000)
        vx = 0.01*rd.randint(-100,100)
        vy = 0.01*rd.randint(-100,100)
        vz = 0.01*rd.randint(-100,100)
        
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
ax.set_xlim3d([-11,11])
ax.set_ylim3d([-11,11])
ax.set_zlim3d([-11,11])
ax.set_title("Scatter Animation")
x,y,z=particle.getcoordinate()
scatter=[ax.scatter3D(x,y,z,color='green')]

anim=animation.FuncAnimation(fig,update_coordinate,40,fargs=(scatter,),interval=50)
plt.show()


