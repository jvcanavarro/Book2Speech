import cv2


def take_picture():
    cam = cv2.VideoCapture(0)
    while True:
        _, frame = cam.read()
        print(frame)

        cv2.imshow("Webcam", frame)
        key = cv2.waitKey(1)

        if key == ord("s"):
            cv2.imwrite(filename="picture.jpg", img=frame)
            picture = cv2.imread("picture.jpg")
            picture = cv2.imshow("Captured Image", picture)
            cv2.waitKey(500)
            cv2.destroyAllWindows()
        elif key == ord("q"):
            cam.release()
            cv2.destroyAllWindows()
            break