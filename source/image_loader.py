import cv2


def capture_image():
    webcam = cv2.VideoCapture(0)
    image = []
    while True:
        flag, frame = webcam.read()
        cv2.imshow('Rasp3 Camera', frame)

        key = cv2.waitKey(1)

        if key == ord('s'):
            # cv2.imwrite(filename='image.jpg', img=frame)
            # image = cv2.imread('image.jpg')
            image = frame
            cv2.imshow('Captured Image', image)
            cv2.waitKey(500)
            cv2.destroyAllWindows()

        if key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            return image


def load_image(filename):
    return cv2.imread(filename)


def load_folder(directory):
    return [cv2.imread(filename) for filename in directory]
