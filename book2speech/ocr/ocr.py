try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from tesserocr import PyTessBaseAPI


def image_to_text(image, lang, use_tesserocr):
    if use_tesserocr:
        with PyTessBaseAPI(lang=lang) as api:
            api.SetImageFile(image)
            text = api.GetUTF8Text()
    else:
        config = "-c tessedit_do_invert=0"
        text = pytesseract.image_to_string(image, lang=lang, config=config)
    return text