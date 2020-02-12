import pytesseract as ocr
import numpy as np
import cv2


def get_grayscaled(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def resize(image, scale=0.5):
    return cv2.resize(image, (0, 0), fx=scale, fy=scale)


def get_text(image, language='por'):
    return ocr.image_to_string(image, lang=language)


def get_threshold(image):
    gray = get_grayscaled(image)
    # reversed = cv2.bitwise_not(gray)
    reversed = gray
    return cv2.threshold(reversed, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


def get_angle(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = - (90 + angle)
    else:
        angle *= -1

    return angle


def deskew(image):
    thresh = get_threshold(image)
    angle = get_angle(thresh)

    h, w = thresh.shape[:2]
    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1)
    return cv2.warpAffine(image, matrix, (h, w), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
