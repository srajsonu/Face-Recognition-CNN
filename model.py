import numpy as npimport cv2from os import listdirfrom os.path import isfile, joindata_path='images/Amit/'files=[f for f in listdir(data_path) if isfile(join(data_path,f))]Training_data,labels=[],[]for i, file in enumerate(files):    image_path=data_path+files[i]    images=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)    Training_data.append(np.asarray(images, dtype=np.uint8))    labels.append(i)labels=np.asarray(labels,dtype=np.int32)model=cv2.face.LBPHFaceRecognizer_create()model.train(np.asarray(Training_data),np.asarray(labels))print('Model Training Completed')face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')def face_detector(img, size=0.5):    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    faces=face_cascade.detectMultiScale(gray,1.3,5)    if faces is None:        return img,[]    roi=[]    for (x,y,w,h) in faces:        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)        roi=img[y:y+h,x:x+w]        roi=cv2.resize(roi,(200,200))    return img, roicap=cv2.VideoCapture(0)while True:    ret,frame=cap.read()    image,face=face_detector(frame)    try:        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)        result=model.predict(face)        if result[1]<500:            confidence=100*(1-(result[1])//300)            display_string=str(confidence)+'%'        cv2.putText(image,display_string,(100,120),cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255))        if confidence > 75:            cv2.putText(image,'Aryan',(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0))            cv2.imshow('Face Cropper',image)        else:            cv2.putText(image,'locked',(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))            cv2.imshow('Face Cropper',image)    except:        cv2.putText(image,'Face Not Found',(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))        #cv2.putText(image,'locked',(250,500),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0))        cv2.imshow('Face Cropper',image)        pass    if cv2.waitKey(1)==13:        breakcap.release()cv2.destroyAllWindows()