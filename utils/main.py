import click
import cv2


@click.command()
@click.option('-filename')
def load(filename):
    image = cv2.imread(filename)
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binary
    thresh = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imshow('', thresh)
    cv2.waitKey(0)

    # Grey Scale
    cv2.imshow('', grey)
    cv2.waitKey(0)

    # Resized
    resize = cv2.resize(image, (0, 0), fx=.8, fy=.8)
    cv2.imshow('', resize)
    cv2.waitKey(0)


if __name__ == '__main__':
    load()
