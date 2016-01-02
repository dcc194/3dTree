import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

imgL1 = cv2.imread('C:/Users/Duane/Documents/Duane/StereoTree/treeL.jpg',0)
imgR1 = cv2.imread('C:/Users/Duane/Documents/Duane/StereoTree/treeR.jpg',0)

scale = 0.3

imgL = cv2.resize(imgL1, (0,0), fx=scale, fy=scale)

imgR = cv2.resize(imgR1, (0,0), fx=scale, fy=scale)

stereo = cv2.StereoBM_create(numDisparities=32, blockSize=5)
disparity = stereo.compute(imgL,imgR)

#plt.imshow(disparity,'gray')
#plt.show()

ind = np.where(disparity > 0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# print ind[0]
# print ind[1]
# print disparity[ind[0],ind[1]]

ax.scatter(ind[0],ind[1],disparity[ind[0],ind[1]], )
plt.show()

print np.size(ind)
print ind

print 'done'