from PIL import Image
import cv2

#starting from this point, the image is converted to computer understable format, or matrix. Printing img will not be understandable

img = cv2.imread("swayam_python\img.jpg")  #creating a object to handle the image

# print(img)  # this gives a matrix form of the image, currently being used by the cpu

clahe = cv2.createCLAHE() # creating an object for using CLAHE

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # converting the color image to gray scale for enhancement

#enhacing the image by enhacning the contrast

final = clahe.apply(gray_img)

cv2.imshow("original: ",img)    #   popping a window to show image
cv2.imshow("enhanced: ",final)
cv2.waitKey(0) #    waiting for the user to manually close the windows 
cv2.destroyAllWindows() #   waits for the popped windowds to close the proceeds to the next line of code and then shows "Done"

# cv2.imwrite("Enhanced.png",final) # saving the <final> image

print("Done")