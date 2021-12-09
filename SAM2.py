import numpy as np
import matplotlib.pyplot as plt
r=plt.imread(r"apple.jpeg")     #匯入照片
r = np.double(r)
d=r[60,150,:]     #要尋找的點、搜尋的圖

#plt.imshow(r)#顯示圖片
r=r.reshape(165*220,-1)  #將r由三維轉二維
b=np.dot(r,d)   #<rd>
rd=np.sum(r*d,1)  #<rd>
# rr=(np.sum(r**2 ,1))**0.5   #||r||
# dd=(np.sum(d**2 ))**0.5     #||d||
# rd=rd.reshape(165,220)
# rr=rr.reshape(165,220)
# m=np.arccos(rd/(rr*dd))
# plt.imshow(m)
