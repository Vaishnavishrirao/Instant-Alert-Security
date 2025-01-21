import cv2
cam = cv2.VideoCapture(0)
res, image= cam.read()
if res:
    # showing result, it take frame name and image
    # output
    cv2.imshow("img", image)

    # saving image in local storage
    cv2.imwrite("C://Users//hi//Desktop//da43//img/img1.png", image)

    # If keyboard interrupt occurs, destroy image
    # window
    cv2.waitKey(0)
    cv2.destroyAllWindows()