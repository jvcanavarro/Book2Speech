import cv2
import pytesseract
from pytesseract import Output

CONFIG = "-c tessedit_do_invert=0"


def image_to_text(image, lang, bbox):
    if type(image) == str:
        image = cv2.imread(image)

    if bbox:
        data = pytesseract.image_to_data(image, output_type=Output.DICT)
        n_boxes = len(data["level"])
        for i in range(n_boxes):
            x, y, w, h = (
                data["left"][i],
                data["top"][i],
                data["width"][i],
                data["height"][i],
            )
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imwrite("output_bb.png", image)

    return pytesseract.image_to_string(image, lang=lang, config=CONFIG)
