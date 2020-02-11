from loader import capture_image, load_image, load_folder
from glob import glob
import processor
import click


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


    deskewed = processor.deskew(image)
    cv2.imshow(deskewed)
    # grey = processor.get_grayscaled(pics)
    # resize = processor.resize(grey)
    # thresh = processor.get_threshold(resize)
    # print(processor.get_text(thresh))


if __name__ == '__main__':
    start()
