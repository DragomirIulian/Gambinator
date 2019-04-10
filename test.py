import cv2
import numpy as np

img = cv2.imread('inputFiles\\raw.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

v = np.median(img)
print(v)

# apply automatic Canny edge detection using the computed median
# lower = int(max(150, (1.0 - sigma) * v))
# upper = int(min(200, (1.0 + sigma) * v))
# print(str(lower) + " " + str(upper))
# edges = cv2.Canny(img, lower, upper)

# linesDiff
# verticalLinesDiff = []
# horizontalLinesDiff = []

# for index, item in enumerate(verticalLines):
#     if(index == 0):
#         verticalLinesDiff.append(verticalLines[0][0])
#     else:
#         verticalLinesDiff.append(verticalLines[index][0] - verticalLines[index-1][0])

# for index, item in enumerate(horizontalLines):
#     if(index == 0):
#         horizontalLinesDiff.append(horizontalLines[0][0])
#     else:
#         horizontalLinesDiff.append(horizontalLines[index][0] - horizontalLines[index-1][0])