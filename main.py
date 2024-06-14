import cv2

cap = cv2.VideoCapture("./video/la_cabra.mp4")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

i = 0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img', frame)
    cv2.waitKey(100)

    frame = cv2.resize(frame, (640,480))
    frame = cv2.flip(frame, 1)
    out.write(frame)
    
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i=i+1

out.release()
cv2.destroyAllWindows()