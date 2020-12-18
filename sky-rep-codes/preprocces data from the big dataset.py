import cv2
import numpy as np
import os


for filename in os.listdir(r'G:\highway'):  
    if filename.endswith('.jpg'):
        img=cv2.imread(r'G:\highway'+r'/'+filename)
        img=cv2.resize(img,(1024,768))
        cv2.imwrite(r'G:\dataset'+r'/'+filename,img)
            
    elif filename.endswith('seg.png'):
        img=cv2.imread(r'G:\highway'+r'/'+filename)
        img=cv2.resize(img,(1024,768))
        lower_blue = np.array([0,115,89])
        upper_blue = np.array([100,117,91])
        
        mask = cv2.inRange(img, lower_blue, upper_blue)
    
        cv2.imwrite(r'G:\dataset'+r'/'+filename,mask)

    
