import cv2
import os
dataset = "dataset"
name = "champ"

path = os.path.join(dataset,name)
if not os.path.isdir(path):
    os.mkdir(path)

(width,height) = (130,100)
alg = "haar-cascade-files-master/haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)
# for local cemera ot works with 1
cam = cv2.VideoCapture(1)

count = 1
while count < 31:
    print(count)
    _, img = cam.read()
    #img = cv2.imread("../Day5-FaceDetect/prav.jpg")

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        faceOnly = grayImg[y:y+h,x:x+w]
        resizeImg = cv2.resize(faceOnly, (width, height))
        cv2.imwrite("%s/%s.jpg" %(path, count), resizeImg)
     #   img2 = cv2.imread("%s/%s.jpg")
      #  print(img2)
        count += 1
    cv2.imshow("FaceDetection", img)
    key = cv2.waitKey(100)
    if key == 27:
        break
print("Image Captured succssfully")
cam.release()
cv2.destroyAllWindows()
