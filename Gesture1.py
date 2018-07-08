import cv2

cap = cv2.VideoCapture(0)

while(True):

   ret,cap1 = cap.read()

   cv2.imshow("frame",cap1)

   key = cv2.waitKey(1) & 0xFF

   if key == ord("q"):

    break

cv2.destroyAllWindows()
cap1.release()
