import cv2

video = cv2.VideoCapture('videos/auto.mp4')
auto = cv2.CascadeClassifier('auto.xml')

output_file = open('output.txt', 'w')

while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = auto.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
    for (x,y,w,h) in img:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
        plate_info = f"Plate detected at coordinates(x: {x}, y: {y}, width: {w}, height: {h})"
        output_file.write(plate_info + '\n')

    cv2.imshow('Video_with_car', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

output_file.close()


