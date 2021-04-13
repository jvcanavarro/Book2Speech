import cv2
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
@click.option("--deskew-image", is_flag=True)
@click.option("--improve-image", is_flag=True)
@click.option("--use-tesserocr", is_flag=True)
@click.option("--verbose", "-v", is_flag=True)
@click.option("--save-results", "-s", "save", is_flag=True)
@click.option("--calculate-metrics", "metrics", is_flag=True)
@click.option("--lang", type=click.Choice(["eng", "por"]), default="por")
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
@click.option(
    "--blur-mode",
    type=click.Choice(
        ["average", "gaussian", "median", "bilateral", "disable"],
    ),
    default="disable",
)
@click.option(
    "--thresh-mode",
    type=click.Choice(
        ["simple", "adaptative", "otsu", "disable"],
    ),
    default="otsu",
)
@click.option("--output", "-o", type=str, default="output")
def parse_parameters(
    image,
    text,
    ocr_text,
    dictionary,
    play_audio,
    disable_tts,
    deskew_image,
    improve_image,
    use_tesserocr,
    verbose,
    save,
    metrics,
    lang,
    correction_mode,
    transform_mode,
    blur_mode,
    thresh_mode,
    output,
):
    # Capture Image
    if not image:
        image = take_picture()

    # Image Processing
    if improve_image:
        image = improve_image_quality(
            image, blur_mode, thresh_mode, deskew_image, output, save
        )

    # Tesseract
    ocr_text = image_to_text(image, lang, use_tesserocr)

    # Text Processing
    true_text = text.readlines()  # text.read().splitlines()
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
    if metrics:
        _ = generate_metrics(transformed_true_text, transformed_ocr_text, verbose)

    # Text to Speech
    if not disable_tts:
        text_to_speech(transformed_ocr_text, output, play_audio)

    # Save Results
    if save:
        with open(output + ".txt", "w") as text_file:
            text_file.write(" ".join(transformed_ocr_text))


if __name__ == "__main__":
    parse_parameters()
