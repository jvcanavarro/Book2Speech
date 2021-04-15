import numpy as np
import cv2

from image_processing.dewarp import dewarp_image


def improve_image_quality(
    image_path, blur_mode, thresh_mode, dewarp, optimizer, output, save
):

    image = (
        dewarp_image(image_path, optimizer, save)
        if dewarp
        else cv2.imread(image_path, 0)
    )

    if blur_mode == "average":
        image = cv2.blur(image, (5, 5))
    elif blur_mode == "gaussian":
        image = cv2.GaussianBlur(image, (5, 5), 0)
    elif blur_mode == "median":
        image = cv2.medianBlur(image, 3)
    elif blur_mode == "bilateral":
        image = cv.bilateralFilter(image, 9, 75, 75)

    if thresh_mode == "simple":
        image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
    elif thresh_mode == "gaussian":
        image = cv2.adaptiveThreshold(
            image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2
        )
    elif thresh_mode == "mean":
        image = cv2.adaptiveThreshold(
            image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 2
        )
    elif thresh_mode == "otsu":
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    if save:
        cv2.imwrite(output + ".png", image)

    # cv2.imshow("image", image)
    # cv2.waitKey(0)

    return image
