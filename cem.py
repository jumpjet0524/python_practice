# a=np.array([1,2,3]).reshape([3,1])
# at=np.transpose(a)
# s=np.dot(a,at)
# ss=a@at
import numpy as np
import matplotlib.pyplot as plt
r=plt.imread(r"C:\Users\jumpj\Google 雲端硬碟\python practice\apple.jpeg")     #匯入照片
r = np.double(r)
d=r[60,150]
dt=d.reshape(1,3)
r=r.reshape(165*220,-1)
rt=r.T
R=np.dot(rt,r)/3
Ri=np.linalg.inv(R)
a=((Ri@d).T)
cem=(r@((Ri@d).T))/(dt@Ri@d)
cem=cem.reshape(165,220)
plt.imshow(cem)