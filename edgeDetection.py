import cv2
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime
import operator

sigma = 0.33
spaceBetweenLinesDistance = 275
deltaDistance = 25

eps = 0.01
theta1 = 0
theta2 = 1.57

photoName = 'outputFiles/' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

def drawLines(lines, img):
    for line in lines:
        (rho,theta) = line
        if(abs(theta-theta1) < eps): 
            drawLine(rho, theta, img)
        elif(abs(theta-theta2) < eps):
            drawLine(rho, theta, img)

def drawLine(rho, theta, img):
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 3000*(-b))
            y1 = int(y0 + 3000*(a))
            x2 = int(x0 - 3000*(-b))
            y2 = int(y0 - 3000*(a))
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),20)

def inRange(distance):
    if((distance > spaceBetweenLinesDistance - deltaDistance) and (distance < spaceBetweenLinesDistance + deltaDistance)):
        return True
    return False

# chess lines will be either vertical or horizontal - 18 lines in total
# the difference between 2 consecutive lines will be spaceBetweenLinesDistance +- deltaDistance (250,300)

def findChessLines(lines):
    if(len(lines) < 9):
        return []
    for index, item in enumerate(lines):
        chessLines = []
        chessLines.append(item)
        currentIndex = index + 1
        while(currentIndex < len(verticalLines)):
            if(inRange(lines[currentIndex][0] - chessLines[len(chessLines) - 1][0])):
                chessLines.append(lines[currentIndex])
                currentIndex += 1
                if(len(chessLines) == 9):
                    return chessLines
            else:
                break
    return []

    
img = cv2.imread('inputFiles\\raw.jpg')
imgCopy = img
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

v = np.median(img)

edges = cv2.Canny(img,150,200)


lines = cv2.HoughLines(edges,10,np.pi/90,800)
linesCount = 0

verticalLines = []
horizontalLines = []
for line in lines:
    for rho,theta in line:
        if(abs(theta-theta1) < eps): 
            verticalLines.append((rho,theta))
            linesCount += 1
            drawLine(rho, theta, imgCopy)
        elif(abs(theta-theta2) < eps):
            horizontalLines.append((rho,theta))
            linesCount += 1
            drawLine(rho, theta, imgCopy)

print(str(len(verticalLines)))
print(str(len(horizontalLines)))

if(len(verticalLines) == 0 or len(horizontalLines) == 0):
    exit()

verticalLines.sort(key=operator.itemgetter(0))
horizontalLines.sort(key=operator.itemgetter(0))

chessBoardVerticalLines = findChessLines(verticalLines)
chessBoardHorizontalLines = findChessLines(horizontalLines)

print('Chessboard lines count')
print(str(len(chessBoardVerticalLines)))
print(str(len(chessBoardHorizontalLines)))

print('Vertical lines: ')
print(*chessBoardVerticalLines)
print('Horizontal lines: ')
print(*chessBoardHorizontalLines)

drawLines(chessBoardVerticalLines, img)
drawLines(chessBoardHorizontalLines, img)


print('Lines count: ' + str(linesCount))
cv2.imwrite(photoName + '-edges.jpg',edges)
cv2.imwrite(photoName + '-rawLines.jpg',img)
cv2.imwrite(photoName + '-lines.jpg',img)



# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()
