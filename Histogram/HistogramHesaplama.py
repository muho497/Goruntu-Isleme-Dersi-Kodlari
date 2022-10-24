from numpy import zeros, shape
from matplotlib import pyplot as plt
import cv2
import numpy as np

deneme = "deneme.jpg"
resim = cv2.imread(deneme)



h = resim.shape[0]
w = resim.shape[1]

Hist = zeros(256);
[w,h] = shape(I);
for v in range (0, u<h):
    for u in range (0, u<w):
        i= I(u,v)
        Hist[i]=Hist[i]+1




