import numpy as np
import cv2


img=cv2.imread("deneme.jpg",0)


#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


a=np.zeros((256,),dtype=np.float16)

height,width=img.shape


for i in range(width):
    for j in range(height):
                  g=img[j,i]
                  a[g]=a[g]+1
print(a)
#hist = cv2.calcHist([img],[0],None,[256],[0,256])
#cv2.imshow('hist',hist)
#cv2.waitKey(0)


#x =range(0,256)
#y =a
#plt.plot(x,y)
#plt.show()


