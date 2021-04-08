import numpy as np
import cv2


def deskew(thresh):
    h, w = thresh.shape[:2]
    coords = np.column_stack(np.where(thresh > 0))
    center = (w // 2, h // 2)

    angle = cv2.minAreaRect(coords)[-1]
    angle = -(90 + angle) if angle < -45 else -angle

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(
        thresh, matrix, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE
    )

    return rotated_image


def improve_image_quality(image_path, output, save):
    original_image = cv2.imread(image_path)
    resized_image = cv2.resize(original_image, (0, 0), fx=0.5, fy=0.5)
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    deskewed_image = deskew(thresh)

    if save:
        cv2.imwrite(output + '.png', thresh)

    return thresh
