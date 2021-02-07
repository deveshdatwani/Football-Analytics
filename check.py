import cv2
import numpy as np

rec = cv2.VideoCapture('assets/GOPR7194.MP4')
height = 600
width = 1000
input_pts = np.float32([[140,570],[800,400],[1400,300],[1350,850]])
output_pts = np.float32([[0,0],[width-1,0],[width-1,height-1],[0,height-1]])
matrix = cv2.getPerspectiveTransform(input_pts,output_pts)

while rec.isOpened():
    ret, frame = rec.read()
    copy_frame = frame.copy()
    cv2.circle(copy_frame, (1300,900), 10, (255,0,0),2) 
    if ret == True:
        frame = cv2.warpPerspective(frame, matrix, (width, height), cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0))         
        cv2.imshow('frame',frame)
        cv2.imshow('frame2',copy_frame)
        
        if cv2.waitKey(25) & 0xff == ord('q'):
            break
    else:
        break

rec.release()
cv2.destroyAllWindows()
