import numpy as np

class particle():
    objects=[]
    def __init__(self,position,velocity):
        self.position=position
        self.velocity=velocity
        self.neighbours=[]
        self.accelaration=(0,0,0)
        particle.objects.append(self)

    def check(self):
        print(self.position)
        print(self.velocity)
    @classmethod
    def update(cls):
        
        for obj in cls.objects:
            x,y,z=obj.position
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
          
          
            vx,vy,vz=obj.velocity
            ax,ay,az=obj.accelaration
            obj.accelaration=(0,0,0)
            obj.position=(x+(vx*0.1),y+(vy*0.1),z+(vz*0.1))
            obj.velocity=(vx+obj.accelaration[0]*0.1,vy+obj.accelaration[1]*0.1,vz+obj.accelaration[2]*0.1)
    @classmethod
    def energy(cls):
        e=0
        for obj in cls.objects:
            e=e+obj.velocity[1]**2+obj.velocity[1]**2+obj.velocity[2]**2
        return ('Energy',e)
            
    @classmethod
    def show(cls):
        for obj in cls.objects:
            print(obj.position,obj.velocity)

    x_list1=[]
    y_list1=[]
    z_list1=[]       

    @classmethod
    def getcoordinate(cls):
                cls.x_list1=[]
                cls.y_list1=[]
                cls.z_list1=[]
                for obj in cls.objects:
                        x,y,z=obj.position
                        cls.x_list1.append(x)
                        cls.y_list1.append(y)
                        cls.z_list1.append(z)
                return (cls.x_list1,cls.y_list1,cls.z_list1)
                        

def create():           
    lists=[]
    for i in range(100):
            lists.append(particle((10*np.random.random(),10*np.random.random(),10*np.random.random()),(np.random.random(),np.random.random(),np.random.random())))

def run():
        create()
        animate_system()
        

def update_coordinate(i,scatter):
        particle.update()
        x,y,z=particle.getcoordinate()
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


