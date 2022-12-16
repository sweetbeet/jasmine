#credit to initial skeleton:webcam-capture-v1.01
# Edited By/ Author: Maryam Azmandian
import cv2 

def preProcess():
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    while True:
        try:
            check, frame = webcam.read()
            print(check) #prints true as long as the webcam is running
            print(frame) #prints matrix values of each framecd 
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("Processing image...")
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)

                # print("Converting RGB image to grayscale...")
                # gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                # print("Converted RGB image to grayscale...")
                # # print("Resizing image to 28x28 scale...")
                # # img_ = cv2.resize(gray,(28,28))
                # # print("Resized...")
                # # My code here:
                # img_deblured = cv2.medianBlur(gray,11)
                # ret,thresh1 = cv2.threshold(img_deblured,75,255,cv2.THRESH_BINARY)
                # # thresh2_adap_gaus = cv2.adaptiveThreshold(img_deblured,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                # # cv2.THRESH_BINARY,11,2)
                # ###
                # # img_done2 = cv2.imwrite(filename='saved_img-final_thresh2Adaptive.jpg', img=thresh2_adap_gaus)
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                cv2.imshow("contours", gray)
                cv2.waitKey(0)
                blurred = cv2.GaussianBlur(gray, (3, 3), 0,cv2.BORDER_DEFAULT)
                cv2.imshow("contours", blurred)
                cv2.waitKey(0)
                edged = cv2.Canny(blurred,100, 200,5)

                # define a (3, 3) structuring element
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))

                # apply the dilation operation to the edged image
                dilate = cv2.dilate(edged, kernel, iterations=1)

                # find the contours in the dilated image
                contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                image_copy =img_.copy()
                # draw the contours on a copy of the original image
                cv2.drawContours(image_copy, contours, -1, (0, 255, 0), 2)
                print(len(contours), "objects were found in this image.")

                cv2.imshow("Dilated image", dilate)
                cv2.imshow("contours", image_copy)
                cv2.waitKey(0)
                dim = (150, 150)
                img_resized = cv2.resize(image_copy, dim, interpolation = cv2.INTER_AREA)
                img_done = cv2.imwrite(filename='saved_img_final.jpg', img=img_resized)
                print("Image saved!")
            
                break
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
            
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
    return contours,image_copy.shape