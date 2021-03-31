import click

from ocr.ocr import image_to_text
from metrics.metrics import generate_metrics
from spellchecker.spellchecker import correct_spelling
from transformations.transformations import apply_transformations


@click.command()
@click.option('--image', '-i', type=click.Path())
@click.option('--text', '-t', type=click.File())
@click.option('--dictionary', '-d', type=click.Path())
@click.option('--correction-mode',
              'mode',
              type=click.Choice(['simple', 'compound', 'segmentation']),
              default='simple')
@click.option('--use-tesserocr', is_flag=True)
@click.option('--calculate-metrics', 'metrics', is_flag=True)
@click.option('--transformation',
              type=click.Choice(['reduced', 'default', 'extended']),
              default='default')
@click.option('--output-text', '-o', 'output', type=str, default='output.txt')
@click.option('--save-results', '-s', 'save', is_flag=True)
def parse_parameters(image, text, dictionary, mode, use_tesserocr, metrics,
                     transformation, output, save):
    # TODO: Image Processing

    # Tesseract
    wrapper = 'tesserocr' if use_tesserocr else 'pytesseract'
    ocr_text = image_to_text(image, wrapper)

    # Text Processing
    true_text = text.readlines()  # text.read().splitlines()
    if dictionary or metrics:
        transformed_true_text, transformed_ocr_text = apply_transformations(
            ocr_text, true_text, transformation)

    if dictionary:
        transformed_ocr_text = correct_spelling(transformed_ocr_text, dictionary, mode)

    # Performance Evaluation
    # TODO: get a list of wrong words/characters
    if metrics:
        _ = generate_metrics(transformed_true_text, transformed_ocr_text)

    # TODO: Text to Speech

    # Save Results
    if save:
        with open(output, 'w') as text_file:
            text_file.write(ocr_text)


if __name__ == '__main__':
    parse_parameters()
