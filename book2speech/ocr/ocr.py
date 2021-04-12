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
        text = pytesseract.image_to_string(image, lang=lang)
    return text