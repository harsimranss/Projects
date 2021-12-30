
class particles():
    objects=[]
    def __init__(self,position,velocity):
        self.position=position
        self.velocity=velocity
        self.acceleration=(0,0,0)
        self.neighbours=[]
        particles.objects.append(self)
    @classmethod
    def update(cls):
        aax=0
        for particle in cls.objects:
            for neighbour in particle.neighbours:
                aax=F+aa
            

            
        
