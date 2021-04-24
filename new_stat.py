import numpy as np 
from numpy import random as rd
import time
timestart=time.process_time()
class particle():

    objects = []
    time=0
    def __init__(self, position, velocity):
        self.position = position
        self.position1=position
        self.velocity = velocity
        self.velocity1=velocity
        self.accelaration1=(0,0,0)
        self.accelaration = (0, 0, 0)
        self.neighbours = []
        self.da=(0,0,0)
        particle.objects.append(self)

    @classmethod
    def update(cls):
        t=0.05
        th=t/2
        # updating neighbours
        if particle.time%200==0:
            particle.update_neighbours()
        # updating accelaration before updating coordinates
        particle.update_ac()
        for obj in cls.objects:
            x, y, z = obj.position
            vx, vy, vz = obj.velocity
            
            if x>50:
                vx,vy,vz=(-abs(vx),vy,vz)
              
            if y>50:
                vx,vy,vz=(vx,-abs(vy),vz)         
               
            if z>50:
                vx,vy,vz=(vx,vy,-abs(vz))
              
            if x<-50:
                vx,vy,vz=(abs(vx),vy,vz)
       
            if y<-50:
                vx,vy,vz=(vx,abs(vy),vz)
          
            if z<-50:
                vx,vy,vz=(vx,vy,abs(vz))
            
            (vx,vy,vz)=(vx + obj.accelaration[0] * th,vy + obj.accelaration[1] * th,vz+ obj.accelaration[2] * th)
     
            obj.position = (x + t * vx, y + t * vy, z + t * vz)
            obj.velocity=(vx,vy,vz)
        particle.update_ac()
        for obj in particle.objects:
            obj.velocity=(obj.velocity[0]+obj.accelaration[0]*th,obj.velocity[1]+obj.accelaration[1]*th,obj.velocity[2]+obj.accelaration[2]*th)
            
        particle.time=particle.time+1
    def force(self):
        kb_m=205
        ep = 0.000515 # Well depth kb_m*T , T= 120K
        d = 1 # sigma
        f = (0, 0, 0)
        R = 1 # boundary of neighbourhood
        
        R = 1 # boundary of neighbourhood
        x0, y0, z0 = self.position
        for obj in self.neighbours:
            x, y, z = obj.position
            r=((x-x0)**2+(y-y0)**2 +(z-z0)**2)**(0.5)
            p = ep * (2 * ((1)/(r**14)) - 1 * ((1)/(r**8)))
            f = (f[0] -p * (x - x0), f[1] - p * (y - y0), f[2] - p * (z - z0))
        # changing accelaration so as to not calculate force for future config.
        self.accelaration=f

    @classmethod
    def update_neighbours(cls):
        R_critical=2.5 # 2.5*Sigma
        
        for obj in cls.objects:
            obj.neighbours=[]
            x,y,z=obj.position
            for obj2 in cls.objects:
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
        return e
        
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
    def getvelocity(cls):
        cls.x_list = []
        cls.y_list = []
        cls.z_list = []

        for obj in cls.objects:
            x, y, z = obj.velocity
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
    xj=0
    yj=1
    zj=1
    v_da=np.load('v_da1.npy',allow_pickle=True)
    for i in range(100):
        xj=xj+1
        if xj%8==0:
            yj=yj+1
            xj=1
        if yj%8==0:
            zj=zj+1
            yj=1
        x = -30+(2**(1/6)*xj)
        y = -30+(2**(1/6)*yj)
        z = -30+(2**(1/6)*zj)
        
        vx,vy,vz=(float(v_da[i][0]),float(v_da[i][1]),float(v_da[i][2]))
        lists.append(particle((x, y, z), (vx, vy, vz)))


## Changing Directory
import os
os.chdir('/home/sarhandi/stat')
t1=time.process_time()
create()
data_set=[]
data_set2=[]
print('Working On it!!')
## creating velocity distribution data of initial values
particle.velocity_distribution1()

print('initial',particle.energy()*(6.27*10**6)/(3*100))
### Simulating system and saving it in data set
t2=time.process_time()
for pp in range(100000):
    particle.update()
    if particle.time%1000==0:
            #print("#", end="")
            data_set.append(particle.getcoordinate())
t3=time.process_time()
data_set.append(particle.getcoordinate())
data_set1=[]
data_set1.append(particle.getvelocity())
print('Wait is Over!!!!')
timeend=time.process_time()
print('Total time taken:',timeend-timestart)
print("Temperature-",particle.energy()*(6.27*10**6)/(3*100))
print(t1,t2,t3)
### Generating Data of velocity distribution after simulation
particle.velocity_distribution()
np.save('data_set.npy',data_set,allow_pickle=True)
np.save('data_set1.npy',data_set1,allow_pickle=True)


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


