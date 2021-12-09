import numpy as np
import matplotlib.pyplot as plt
r=plt.imread(r"apple.jpeg")     #匯入照片
r = np.double(r)
d=r[57,158]     #要尋找的點、搜尋的圖
#plt.imshow(r)#顯示圖片
r=r.reshape(165*220,3)  #將r由三維轉二維
a=np.zeros([165*220]) #建立a為165*220*1內容全為0的陣列
for x in range(0,36300):    
       a[x]=r[x,0]*d[0]+r[x,1]*d[1]+r[x,2]*d[2]
  
b=np.zeros([165*220]) #建立a為165*220*1內容全為0的陣列     
for x in range(0,36300):
    b[x]=((r[x,0])**2+(r[x,1])**2+(r[x,2])**2)**0.5
e=((d[0])**2+(d[1])**2+(d[2])**2)**0.5  #||d||
a=a.reshape(165,220)
b=b.reshape(165,220)
m=np.arccos(a/(b*e))
#plt.imshow(m, 'gray')