import cv2
import numpy as np
import math
import sys,skvideo.io

def partition(hull,h_contour):

    hull_partitioned = []
    i = 0
    print(hull.shape[0])

    while i < hull.shape[0]:


        hull_x_net = h_contour[hull[i][0]][0][0]
        hull_y_net = h_contour[hull[i][0]][0][1]
        #start_x_net = h_contour[s][0][
        #start_y_net = h_contour[s][0][1]
        #end_x_net = h_contour[e][0][0]
        #end_y_net = h_contour[e][0][1]
        j = i+1
        while j < hull.shape[0]:
            dist = math.sqrt((hull_x_net-h_contour[hull[j][0]][0][0])**2 + (hull_y_net-h_contour[hull[j][0]][0][1])**2)
            if(dist<=50):
                hull = np.delete(hull,j,0)
                j-=1
            j+=1

        i+=1

        #defects_partitioned.append([[[int(start_x_net),int(start_y_net)],[int(end_x_net),int(end_y_net)],[int(far_x_net),int(far_y_net)],d]])

    #defects_partitioned = np.asarray(defects_partitioned)
    return(hull)

def find_number(defects,h_contour):

    count = 0

    for i in range(0,defects.shape[0]):
        s,e,f,d = defects[i,0]
        if(i==defects.shape[0]-1):
            s1,e1,f1,d1 = defects[0,0]
        else:
            s1,e1,f1,d1 = defects[i+1,0]

        dist_defects = ((h_contour[f1][0][0]-h_contour[f][0][0])**2 + (h_contour[f1][0][1]-h_contour[f][0][1])**2)

        a_2 = ((h_contour[e][0][0]-h_contour[f][0][0])**2 + (h_contour[e][0][1]-h_contour[f][0][1])**2)

        b_2 = ((h_contour[e][0][0]-h_contour[f1][0][0])**2 +(h_contour[e][0][1]-h_contour[f1][0][1])**2)

        slope_net = (a_2+b_2-dist_defects)/(2*math.sqrt(a_2)*math.sqrt(b_2))

        slope_net = math.degrees(math.acos(slope_net))

        if(slope_net<=60):
            count+=1
            #print("The angle is:%d and the index is%d"%(slope_net,i))

    return(count)


# Sample image we took

cap = cv2.VideoCapture('hello2.webm')
f = open('Contour.txt','w')


while(True):
     ret,cap1 = cap.read()
     cv2.imshow("frame",cap1)
     key = cv2.waitKey(1) & 0xFF
     if key == ord("q"):
       break
     if(ret==True):
       hsv = cv2.cvtColor(cap1,cv2.COLOR_BGR2HSV)

#Defining Ranges of skin color in hsv
       lower_blue = np.array([0,0,0])
       upper_blue = np.array([180,255,100])

#Thresholding only to obatin skin cvtColor
       mask=cv2.inRange(hsv,(0,20,70),(20,255,255))
       cv2.imshow("Black And White",mask)

       kernel = np.ones((3,3),np.uint8)
       mask = cv2.dilate(mask,kernel,iterations = 4)
       #mask = cv2.GaussianBlur(mask,(5,5),100)
       """

          It can only be applied to black and white images, i have used dilate
          function which kind of expands the image, so henceforth more area for consideration
        """


       image,contours,hierarchy = cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
       contours1 = np.copy(contours)

  # Please this area is the main working code..
       max_area = 0
       largest_contour=-1
       for i in range(len(contours1)):
          contour = contours1[i]
          area = cv2.contourArea(contour)
          if(area>max_area) :
             max_area=area
             largest_contour=i
       h_contour = contours1[largest_contour]

# Please draw the lines in color RGB space
       #cv2.drawContours(cap1,contours,largest_contour,(0,255,0),2)
       #cap0 = cv2.resize(cap1,(960,540))
       #cv2.imshow('Hand Contours',cap0)

       hull = cv2.convexHull(h_contour,returnPoints =False)
       hull = partition(hull,h_contour)
       hull_points = []

       """ drawing circles of hull points"""

       for i in hull:
           cv2.circle(cap1,tuple(h_contour[i[0]][0]),20,(255,0,0),1)


       defects = cv2.convexityDefects(h_contour,hull)


       """
       Testing sake.... for approximately measuring the distance between two points.

       h_contours[1][0] gives the corrdinates in the figure. the figure cannot be
       resized.

       f.write(str(h_contour[1]))
       f.write(str(h_contour[2]))
       f.write("\n")
       cv2.circle(cap1,tuple(h_contour[1][0]),10,(0,0,255),-1)
       cv2.circle(cap1,tuple(h_contour[2][0]),10,(0,0,255),-1)
       cv2.imshow("With selection points",cap1)
       """
       for i in range(defects.shape[0]) :
           s,e,f,d = defects[i,0]
           start = tuple(h_contour[s][0])
           hull_points.append(start)
           end = tuple(h_contour[e][0])
           far = tuple(h_contour[f][0])
           cv2.line(cap1,start,far,(0,255,0),5)
           cv2.line(cap1,far,end,(0,255,0),5)
           cv2.circle(cap1,far,10,(0,0,255),1)

       cv2.imshow('finally',cap1)

       number = find_number(defects,h_contour)

       print("The Number is %d"%(number))


     else:
        break

cv2.destroyAllWindows()
cap.release()
