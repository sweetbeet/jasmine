# Author: Suhaib SK
# Other contributors: Maryam Azmandian
import cv2
import numpy as np
import webcamPreprocess


# webcamPreprocess.preProcess()
# ## Press s on the terminal to save the photo and run preprocessing
# ## Saves the final image as "saved_img_final.jpg"
# webcamProcessedImg = cv2.imread("saved_img_final.jpg", cv2.IMREAD_UNCHANGED)
# cv2.imshow('Contours', webcamProcessedImg)
# cv2.waitKey(0)
# thresh_image = webcamProcessedImg.astype(np.uint8)

""" # previous code
img = cv2.imread(r"C:sersuhaiycharmProjectsJasminUntitled.png") ## image path
dim = (150, 150)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#convert img to grey
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#set a thresh
thresh = 0
#get threshold image
ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow('sample',thresh_img)
cv2.waitKey(0)
"""


#find contours
# contours, hierarchy = cv2.findContours(webcamProcessedImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(contours)
# #create an empty image for contours
# image = np.zeros(webcamProcessedImg.shape)
# print(len(contours))
# # draw the contours on the empty image
# cv2.drawContours(image, contours, -1, (0,255,0), 3)
# #save image
# cv2.imshow('Contours', image)
# cv2.waitKey(0)
contours,Img_shape = webcamPreprocess.preProcess()
x_scaler = Img_shape[1] / 150
y_scaler = Img_shape[0] / 150
scaler = max(x_scaler, y_scaler)
left_x = 0
left_y = 0
gcode = "G00 X0 Y0\n"
gcode = gcode + f"M03 S250 \n"
j=0
for contour in contours:
    i = 1
    gcode = gcode + f"G00 X{contours[j][0][0][0] / scaler + left_x} Y{contours[j][0][0][1] / scaler + left_y};\n"
    # print(len(contour))
    gcode = gcode + f"M03 S0 \n"
    gcode = gcode + f"G04 P1\n"
    while i < len(contour):
        x = contour[i][0][0] / scaler
        y = contour[i][0][1] / scaler
        code = f"G00  X{x + left_x} Y{y + left_y};\n"
        gcode = gcode + code
        i = i + 1
    gcode = gcode + f"M03 S250 \n"
    gcode = gcode + f"G04 P1 \n"
    if j<=len(contours):
        j=j+1
gcode = gcode + f"G00 X0 Y0"
print(gcode)
path = r'C:\Users\suhai\PycharmProjects\Jasmin\gcode.nc'
f = open('gcode.nc', 'w')
f.write(gcode)