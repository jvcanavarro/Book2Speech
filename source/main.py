from image_loader import capture_image, load_image, load_folder
from image_processor import process_image
from glob import glob
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

    # pre processing: dewarping, gray scale, etc.
    processed_pics = [process_image(pic) for pic in pics]



if __name__ == '__main__':
    start()
