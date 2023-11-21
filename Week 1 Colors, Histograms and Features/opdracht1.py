from skimage.color import rgb2hsv
from skimage.color import hsv2rgb
import matplotlib.pyplot as plt
from skimage import io


def GreyExceptRed(image):
    hsv_img = rgb2hsv(image)
    for x in range(len(hsv_img[:, :, 0])):
        for y in range(len(hsv_img[:, :, 0][x])):
            if 0.05 < hsv_img[:, :, 0][x][y] < 0.95:
                hsv_img[:, :, 1][x][y] = 0.0

    newImage = hsv2rgb(hsv_img)
    histoFromImage(newImage)


def histoFromImage(plot_image):
    hue_img = plot_image[:, :, 0]

    fig, (histo, img) = plt.subplots(ncols=2, figsize=(8, 3))

    histo.hist(hue_img.ravel(), 50)
    histo.set_title("Histogram of the Hue channel")
    img.imshow(plot_image)
    img.set_title("image used")
    plt.show()


image = io.imread('balloon.jpg')

histoFromImage(rgb2hsv(image))

GreyExceptRed(image)