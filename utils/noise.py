import os

import click
import cv2
import numpy as np


@click.command()
@click.option("--image", "im", type=click.Path())
@click.option(
    "--noise",
    type=click.Choice(["gauss", "sep", "poisson", "speckle"]),
    default="gauss",
)
def add_noise(noise, im):
    image = cv2.imread(im, 0)
    
    if noise == "gauss":
        row, col = image.shape
        mean = 1
        var = 10
        sigma = var ** 0.1
        gauss = np.random.normal(mean, sigma, (row, col))
        gauss = gauss.reshape(row, col)
        noisy = image + gauss
    elif noise == "sep":
        row, col = image.shape
        s_vs_p = 0.5
        amount = 0.004
        noisy = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
        noisy[coords] = 1
        # Pepper mode
        num_pepper = np.ceil(amount * image.size * (1.0 - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
        noisy[coords] = 0
    elif noise == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
    elif noise == "speckle":
        row, col = image.shape
        gauss = np.random.randn(row, col)
        gauss = gauss.reshape(row, col)
        noisy = image * gauss
    
    cv2.normalize(noisy, noisy, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    noisy = noisy.astype(np.uint8)
    cv2.imshow("noise", noisy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    add_noise()
