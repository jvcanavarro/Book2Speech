import click

from ocr.ocr import image_to_text
from tts.tts import text_to_speech
from metrics.metrics import generate_metrics
from spellchecker.spellchecker import correct_spelling
from transformations.transformations import apply_transformations
from image_processing.image_processing import improve_image_quality
# pylint: disable=no-value-for-parameter


@click.command()
@click.option('--text', '-t', type=click.File())
@click.option('--image', '-i', type=click.Path())
@click.option('--dictionary', '-d', type=click.Path())
@click.option('--play-audio', is_flag=True)
@click.option('--disable-tts', is_flag=True)
@click.option('--use-tesserocr', is_flag=True)
@click.option('--save-results', '-s', 'save', is_flag=True)
@click.option('--calculate-metrics', 'metrics', is_flag=True)
@click.option('--correction-mode',
              'mode',
              type=click.Choice(['simple', 'compound', 'segmentation']),
              default='simple')
@click.option('--transformation',
              type=click.Choice(['reduced', 'default', 'extended']),
              default='default')
@click.option('--output-text', '-o', 'output', type=str, default='output.txt')
def parse_parameters(image, text, dictionary, play_audio, disable_tts, mode,
                     use_tesserocr, metrics, transformation, output, save):
    # TODO: Image Processing

    # Tesseract
    wrapper = 'tesserocr' if use_tesserocr else 'pytesseract'
    ocr_text = image_to_text(image, wrapper)

    # Text Processing
    true_text = text.readlines()  # text.read().splitlines()
    # Transformations
    if dictionary or metrics:
        transformed_true_text, transformed_ocr_text = apply_transformations(
            ocr_text, true_text, transformation)
    # Spell Checker
    if dictionary:
        transformed_ocr_text = correct_spelling(transformed_ocr_text,
                                                dictionary, mode)

    # Performance Evaluation
    # TODO: get a list of wrong words/characters
    if metrics:
        _ = generate_metrics(transformed_true_text, transformed_ocr_text)

    # TODO: Text to Speech
    if not disable_tts:
        text_to_speech(transformed_ocr_text, output, play_audio)

    # Save Results
    if save:
        with open(output, 'w') as text_file:
            text_file.write(ocr_text)


if __name__ == '__main__':
    parse_parameters()
