import click
from ocr.ocr import image_to_text


@click.command()
@click.option('--image', '-i', type=click.Path('rb'))
@click.option('--text', '-t', type=click.File('rb'))
def parse_parameters(image, text):
    ocr_text = image_to_text(image)
    print(ocr_text)


if __name__ == '__main__':
    parse_parameters()