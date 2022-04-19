import cv2
 
cap = cv2.VideoCapture('VDO CCTV/CCTV 5.mp4')
 
cv2.namedWindow("Test")
 
img_counter = 0
 
while True:
    ret, frame = cap.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Test", frame)
 
    k = cv2.waitKey(5)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "ImagesCar_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
 
cap.release()
cv2.destroyAllWindows()