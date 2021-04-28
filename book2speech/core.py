import cv2
import time
import click
import constants

from ocr.ocr import image_to_text
from tts.tts import text_to_speech
from camera.camera import take_picture
from metrics.metrics import generate_metrics
from spellchecker.spellchecker import correct_spelling
from plot.confusion_matrix import generate_confusion_matrix
from transformations.transformations import apply_transformations
from image_processing.image_processing import improve_image_quality

# pylint: disable=no-value-for-parameter


@click.command()
@click.option("--text", "-t", type=click.Path())
@click.option("--image", "-i", type=click.Path())
@click.option("--bigram", "-b", type=click.Path())
@click.option("--dictionary", "-d", type=click.Path())
@click.option("--dewarp", is_flag=True)
@click.option("--play-audio", is_flag=True)
@click.option("--disable-tts", is_flag=True)
@click.option("--improve-image", is_flag=True)
@click.option("--verbose", "-v", is_flag=True)
@click.option("--debug", "debug", is_flag=True)
@click.option("--confusion-matrix", is_flag=True)
@click.option("--bound-box", "bbox", is_flag=True)
@click.option("--calculate-metrics", "metrics", is_flag=True)
@click.option("--save-results", "-s", "save", is_flag=True)
@click.option("--lang", type=click.Choice(["eng", "por"]), default="eng")
@click.option(
    "--correction-mode",
    type=click.Choice(constants.CORRECTIONS),
    default="simple",
)
@click.option(
    "--transform-mode",
    type=click.Choice(constants.TRANSFORMATIONS),
    default="default",
)
@click.option(
    "--blur-mode",
    type=click.Choice(constants.BLURS),
    default="disable",
)
@click.option(
    "--thresh-mode",
    type=click.Choice(constants.THRESHS),
    default="disable",
)
@click.option(
    "--optimizer",
    type=click.Choice(constants.OPTIMIZERS, case_sensitive=False),
    default="disable",
)
@click.option("--output", "-o", type=str, default="output")
def parse_parameters(
    image,
    text,
    bigram,
    dictionary,
    dewarp,
    play_audio,
    disable_tts,
    improve_image,
    verbose,
    debug,
    confusion_matrix,
    bbox,
    metrics,
    save,
    lang,
    correction_mode,
    transform_mode,
    blur_mode,
    thresh_mode,
    optimizer,
    output,
):
    start = time.time()

    # Capture Image
    if not image:
        image = take_picture()
    image_path = image

    # Image Processing
    if improve_image:
        image = improve_image_quality(
            image, blur_mode, thresh_mode, dewarp, optimizer, output, save
        )

    # Tesseract
    ocr_text = image_to_text(image, lang, bbox)

    # Text Processing
    true_text = open(text).readlines()  # text.read().splitlines()
    # Transformations
    if dictionary or metrics:
        transformed_true_text, transformed_ocr_text = apply_transformations(
            true_text, ocr_text, transform_mode
        )
    # Spell Checker
    if dictionary:
        transformed_ocr_text = correct_spelling(
            transformed_ocr_text,
            dictionary,
            bigram,
            correction_mode,
        )

    end = time.time()
    ellapsed = end - start

    # Performance Evaluation
    if metrics:
        metrics = generate_metrics(transformed_true_text, transformed_ocr_text, verbose)

    # Generate Confusion Matrix
    if confusion_matrix:
        _ = generate_confusion_matrix(metrics, verbose)

    # Text to Speech
    if not disable_tts:
        text_to_speech(transformed_ocr_text, output, play_audio)

    # Save locals to file
    if debug:
        vals = []
        for key in constants.KEYS:
            vals.append(locals()[key])
        for metric in constants.METRICS:
            vals.append(metrics[metric])
        vals.append("\n")

        with open("../results/results", "a") as result:
            result.write(",".join(str(val) for val in vals))

    # Save Results
    if save:
        with open(output + ".txt", "w") as text_file:
            text_file.write(" ".join(transformed_ocr_text))


if __name__ == "__main__":
    parse_parameters()
