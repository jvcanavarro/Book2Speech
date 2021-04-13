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


def improve_image_quality(
    image_path, blur_mode, thresh_mode, deskew_image, output, save
):
    image = cv2.imread(image_path, 0)

    if blur_mode == "average":
        image = cv2.blur(image, (5, 5))
    elif blur_mode == "gaussian":
        image = cv2.GaussianBlur(image, (5, 5), 0)
    elif blur_mode == "median":
        image = cv2.medianBlur(image, 3)
    elif blur_mode == "bilateral":
        image = cv.bilateralFilter(image, 9, 75, 75)

    if thresh_mode == "simple":
        image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    elif thresh_mode == "adaptative":
        image = cv2.adaptiveThreshold(
            image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2
        )
    elif thresh_mode == "otsu":
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    if deskew_image:
        image = deskew(image)

    if save:
        cv2.imwrite(output + ".png", image)

    return image
