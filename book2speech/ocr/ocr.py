import pytesseract


def image_to_text(image, lang):
    config = "-c tessedit_do_invert=0"
    return pytesseract.image_to_string(image, lang=lang, config=config)