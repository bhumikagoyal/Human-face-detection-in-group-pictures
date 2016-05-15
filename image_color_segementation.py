import sys
sys.path.append('/usr/local/lib/python3.4/site-packages')
import cv2
#import cv2.cv as cv
import numpy as np
frameResize=cv2.imread("i4.jpg")
img = cv2.resize(frameResize, (400, 300))
#convert RGB pixel value to YCrCb 
img = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
for x in range(0,299):
	for y in range (0,399):
		if ((img[x,y][2]>=77 and img[x,y][2]<=127 and img[x,y][1]>=133 and img[x,y][1]<=173)):
		   	img[x,y]=255
		else:
			img[x,y]=0

cv2.imshow("Color Segmentation",img)
#Morphological
kernel=np.ones((7,7),np.uint8);
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('gray_image1.png',img)
'''
ret,thresh = cv2.threshold(img,127,255,1)

image,contours,h = cv2.findContours(thresh,1,2)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print len(approx)
    if len(approx)==5:
        print "pentagon"
        cv2.drawContours(img,[cnt],0,255,-1)
    elif len(approx)==3:
        print "triangle"
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
        print "square"
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
    elif len(approx) == 9:
        print "half-circle"
        cv2.drawContours(img,[cnt],0,(255,255,0),-1)
    elif len(approx) > 15:
        print "circle"
   
     cv2.drawContours(img,[cnt],0,(0,255,255),-1)
'''
#Blob

# Setup SimpleBlobDetector parameters.
#params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
#params.minThreshold = 10;
#params.maxThreshold = 200;
 
# Filter by Area.
#params.filterByArea = True
#params.minArea = 1500
'''
#contor
ret,thresh = cv2.threshold(img,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    rect = cv2.boundingRect(c)
    if rect[2] < 100 or rect[3] < 100: continue
    print cv2.contourArea(c)
    x,y,w,h = rect
    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(im,'Moth Detected',(x+w+10,y+h),0,0.3,(0,255,0))

'''
'''
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cnt = contours[0]

ret,thresh = cv2.threshold(img,127,255,0)
contours, _ = cv2.findContours(thresh,cv2.CV_RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    rect = cv2.boundingRect(c)
    if rect[2] < 100 or rect[3] < 100: continue
    print cv2.contourArea(c)
    x,y,w,h = rect
    cv2.rectangle(thresh,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(im,'Moth Detected',(x+w+10,y+h),0,0.3,(0,255,0))
'''
'''
circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,10,param1=50,param2=30,minRadius=34,maxRadius=50)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
'''
cv2.imshow("Image segmentation",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#for x in range(500):
	#for y in range(500):
		#print img[300,x] 
