from cProfile import label
import numpy as np
import cv2 as cv

haar_cascade=cv.CascadeClassifier('haar_face.xml')

people=['Virat','Karan','Sidhu']

# features=np.load('features.npy',allow_pickle=True)
# labels=np.load('labels.npy')

face_recognizer=cv.face.LBPHFacerecognizer_create()
face_recognizer.read('face_trained.yml')

img=cv.imread(r'C:\Users\hp\Desktop\face detection\celebs\Virat\C:\Users\hp\Desktop\face detection\celebs\Virat\Vk3.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('person',gray)

# detect the faces in the image 

faces_rect=haar_cascade.detectMultiscale(gray,1.1,4)

for(x,y,w,h) in faces_rect:
    faces_roi=gray[y:y+h,x:x+h]


    label,confidence=face_recognizer.predict(faces_roi)
    print(f'Label= {people[label]} with a confidence of [confidence]')

    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
            
cv.imshow('detected face',img)
cv.waitKey(0)

# for i in os.listdir(r'C:\Users\hp\Desktop\face detection\celebs'):
#   p.append(i)

# print(p)    