from image_loader import capture_image, load_image, load_folder
from glob import glob
import image_loader
import click


@click.command()
@click.option('-i', '--image', type=click.Path(exists=True))
@click.option('-p', '--path', type=click.Path(exists=True))
def start(image, path):
    if image:
        pic = load_image(image)
    elif path:
        files = glob(path + '*jpg') + glob(path + '*png')
        pic = load_folder(files)
    else:
        pic = capture_image()

    print(len(pic))




if __name__ == '__main__':
    start()
