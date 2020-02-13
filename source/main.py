from loader import capture_image, load_image, load_folder
from glob import glob
import processor
import click
import time
import cv2

@click.command()
@click.option('-i', '--image', type=click.Path(exists=True))
@click.option('-p', '--path', type=click.Path(exists=True))
def start(image, path):

    # loading images
    if image:
        pics = load_image(image)
    elif path:
        files = glob(path + '*jpg') + glob(path + '*png')
        pics = load_folder(files)
    else:
        pics = capture_image()

    # pre processing

    # grey = processor.get_grayscaled(pics)
    # resize = processor.resize(grey)
    # thresh = processor.get_threshold(resize)

    # ocring
    text = processor.get_text(pics)
    print(text)
    processor.write_text(text, 'result.txt')
    #ttsing


if __name__ == '__main__':
    start()
