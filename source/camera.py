import cv2


def capture_image():
    webcam = cv2.VideoCapture(0)
    while True:
        flag, frame = webcam.read()
        cv2.imshow('Rasp3 Camera', frame)

        image = []
        key = cv2.waitKey(1)

        if key == ord('s'):
            cv2.imwrite(filename='image.jpg', img=frame)
            image = cv2.imread('image.jpg')
            image = cv2.imshow('Captured Image', image)
            cv2.waitKey(500)
            cv2.destroyAllWindows()

        if key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            return 'image.jpg'
