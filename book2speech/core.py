import cv2
import sys
import click

from ocr.ocr import image_to_text
from tts.tts import text_to_speech
from camera.camera import take_picture
from metrics.metrics import generate_metrics
from spellchecker.spellchecker import correct_spelling
from transformations.transformations import apply_transformations
from image_processing.image_processing import improve_image_quality

# pylint: disable=no-value-for-parameter


@click.command()
@click.option("--text", "-t", type=click.File())
@click.option("--image", "-i", type=click.Path())
@click.option("--ocr-text", "-ot", type=click.File())
@click.option("--dictionary", "-d", type=click.Path())
@click.option("--play-audio", is_flag=True)
@click.option("--disable-tts", is_flag=True)
@click.option("--only-metrics", is_flag=True)
@click.option("--improve-image", is_flag=True)
@click.option("--use-tesserocr", is_flag=True)
@click.option("--save-results", "-s", "save", is_flag=True)
@click.option("--calculate-metrics", "metrics", is_flag=True)
@click.option("--lang", "-l", type=click.Choice(["eng", "por"]), default="por")
@click.option(
    "--correction-mode",
    type=click.Choice(["simple", "compound", "segmentation"]),
    default="simple",
)
@click.option(
    "--transform-mode",
    type=click.Choice(["reduced", "default", "extended"]),
    default="default",
)
@click.option("--output", "-o", type=str, default="output")
def parse_parameters(
    image,
    text,
    ocr_text,
    dictionary,
    play_audio,
    disable_tts,
    only_metrics,
    improve_image,
    use_tesserocr,
    save,
    metrics,
    lang,
    correction_mode,
    transform_mode,
    output,
):
    true_text = text.readlines()  # text.read().splitlines()

    if only_metrics:
        ocr_text = ocr_text.readlines()
        transformed_true_text, transformed_ocr_text = apply_transformations(
            ocr_text, true_text, transform_mode
        )
        _ = generate_metrics(transformed_true_text, transformed_ocr_text)
        sys.exit()

    # Image Capture
    if not image:
        image = take_picture()

    # Image Processing
    if improve_image:
        image = improve_image_quality(image, output, save)

    # Tesseract
    ocr_text = image_to_text(image, lang, use_tesserocr)

    # Text Processing
    # Transformations
    if dictionary or metrics:
        transformed_true_text, transformed_ocr_text = apply_transformations(
            ocr_text, true_text, transform_mode
        )
    # Spell Checker
    if dictionary:
        transformed_ocr_text = correct_spelling(
            transformed_ocr_text,
            dictionary,
            correction_mode,
        )

    # Performance Evaluation
    # TODO: get a list of wrong words/characters
    if metrics:
        _ = generate_metrics(transformed_true_text, transformed_ocr_text)

    # Text to Speech
    if not disable_tts:
        text_to_speech(transformed_ocr_text, output, play_audio)

    # Save Results
    if save:
        with open(output + ".txt", "w") as text_file:
            text_file.write(ocr_text)


if __name__ == "__main__":
    parse_parameters()
