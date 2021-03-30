import click
from ocr.ocr import image_to_text
from metrics.metrics import calculate_metrics


@click.command()
@click.option('--image', '-i', type=click.Path())
@click.option('--text', '-t', type=click.File())
@click.option('--use-tesserocr', is_flag=True)
@click.option('--calculate-metrics', 'metrics', is_flag=True)
@click.option('--extend-transformations', is_flag=True)
@click.option('--output-text', '-ot', 'output', type=str, default='output.txt')
def parse_parameters(image, text, use_tesserocr, metrics, extend_transformations, output):
    # TODO: Image Processing

    # Tesseract
    wrapper = 'tesserocr' if use_tesserocr else 'pytesseract'
    ocr_text = image_to_text(image, wrapper) 

    # TODO: Text Processing

    # Performance Evaluation
    # TODO: read X readlines
    true_text = text.readlines() # text.read().splitlines()
    if metrics:
        errors = calculate_metrics(true_text, ocr_text, extend_transformations)

    # TODO: Text to Speech

    # Save Results
    with open(output, 'w') as text_file:
        text_file.write(ocr_text)


if __name__ == '__main__':
    parse_parameters()