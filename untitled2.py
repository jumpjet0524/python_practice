#ED
import numpy as np
import matplotlib.pyplot as plt
r=np.double(plt.imread(r"C:\Users\jumpj\Downloads\apple.jpg"))
d=r[57,158]  
r=r.reshape(-1,3)
a=(r-d)**2
b=(np.sum(a,1))**0.5
b=b.reshape(165,220)
plt.imshow(b)
