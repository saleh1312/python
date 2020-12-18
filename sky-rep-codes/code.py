import cv2
import numpy as np 
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from numpy import argmax
import func

model=load_model('model.h5')
wall=cv2.imread(r'test\yu3.jpg')

#4,img23,1,img4
img=cv2.imread(r'test\1.jpg')
img=cv2.resize(img,(900,600))

h,w,c=img.shape
wall= cv2.resize(wall,(w,h))

resi=cv2.resize(img, (256,256))
y2=model.predict((np.reshape(resi,(1,256,256,3)).astype('float32')))
y2=y2*255.0
y2=y2.astype('uint8')
y2=np.reshape(y2[0],(256,256))
y2=cv2.resize(y2, (w,h))
ret,y2 = cv2.threshold(y2,5,255,cv2.THRESH_BINARY)

mask_grund=y2.copy()
        
        
k= np.ones((5,5), np.uint8) 
skye=mask_grund.copy()
mask_grund=cv2.bitwise_not(mask_grund)

mask_grund = cv2.dilate(mask_grund, k, iterations=3) 
mask_grund = cv2.erode(mask_grund, k, iterations=1) 
        
_, contours,_= cv2.findContours(mask_grund.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
 
c = max(contours, key = cv2.contourArea)
x,y,wb,hb = cv2.boundingRect(c)
        
land_mask=mask_grund[y:y+hb,x:x+wb]
land=img[y:y+hb,x:x+wb]
       
        
     
center2 = (int(x+wb/2),int(y+hb/2))
  
output = cv2.seamlessClone(land, wall, land_mask, center2, cv2.NORMAL_CLONE)

cv2.imshow('img',img)
cv2.imshow('wall',wall)
cv2.imshow('output',output)
cv2.imshow('mask-sky',skye)
cv2.waitKey(0)

cv2.destroyAllWindows()
        