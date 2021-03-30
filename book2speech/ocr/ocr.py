try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from tesserocr import PyTessBaseAPI


def image_to_text(image, wrapper, verbose=False):
    if wrapper == 'pytesseract':
        text = pytesseract.image_to_string(image, lang='por')
        if verbose:
            # TODO
            pass

    elif wrapper == 'tesserocr':
        with PyTessBaseAPI(lang='por') as api:
            api.SetImageFile(image)
            text = api.GetUTF8Text()

    else: 
        print("Invalid Tesseract wrapper")

    return text