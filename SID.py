import numpy as np
import matplotlib.pyplot as plt
r=plt.imread(r"C:\Users\jumpj\Google 雲端硬碟\python practice\apple.jpeg")
#plt.imshow(r[...,0])
r=r.astype('uint16')
d=r[60,150].astype('uint16')  #要尋找的點、搜尋的圖,轉換型別，2的10次方避免溢位
r=r.reshape(165*220,-1)
m=np.zeros([165*220,3])
Dr=np.zeros([165*220])
Dd=np.zeros([165*220])
nn=d[2]+d[1]+d[0]
n=d/nn

for y in range(0,165*220):
    for x in range(0, 3):
        m[y][x]=r[y][x]/(r[y][0]+r[y][1]+r[y][2])

for i in range(0, 165*220):
    Dr[i]=m[i][0]*np.log(m[i][0]/n[0])+m[i][1]*np.log(m[i][1]/n[1])+m[i][2]*np.log(m[i][2]/n[2])

for i in range(0, 165*220):
    Dd[i]=n[0]*np.log(n[0]/m[i][0])+n[1]*np.log(n[1]/m[i][1])+n[2]*np.log(n[2]/m[i][2])

sid=Dr+Dd
sid=sid.reshape(165,220)

plt.imshow(sid)