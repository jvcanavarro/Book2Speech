import click
import cv2


@click.command()
@click.option('-filename')
def load(filename):
    image = cv2.imread(filename)

    # Grey Scale
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('', grey)
    cv2.waitKey(500)

    # Binary
    thresh = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imshow('', thresh)
    cv2.waitKey(500)

    # Resized
    cv2.imshow('', cv2.resize(image, (0, 0), fx=.5, fy=.5))
    cv2.waitKey(500)


if __name__ == '__main__':
    load()
