import numpy as np
import matplotlib.pyplot as plt
print("Hello Harsimran")
a,b,c=plt.hist(np.random.binomial(1000,0.9,100000),bins=range(900,1001))
plt.close()
plt.figure(2)
plt.plot(range(900,1000),a)
plt.show()
#gurbiroid gall bngyi

