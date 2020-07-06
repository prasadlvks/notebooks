import numpy
import cv2
imgpath = "C:\\Users\\v-prlakk\\Documents\\pythonscripts\leno.png"
img1 = cv2.imread(imgpath,1)
img2 = numpy.ones((512,512,3),numpy.uint8)
cv2.circle(img2,(266,266),100,(255,0,0),2)
cv2.circle(img2,(266,266),120,(0,255,0),2)
cv2.circle(img2,(266,266),130,(0,0,255),2)
print(numpy.__version__)
print(cv2.__version__)
cv2.imshow('Leno',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()