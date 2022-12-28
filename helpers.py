import itertools
from PIL import Image, ImageDraw


def generate_mandelbrot(c: float) -> float:
    z, n = 0, 0
    global max_iterations
    max_iterations = 80
    while abs(z) <= 2 and n <= max_iterations:
        z = z**2 + c
        n += 1
    return n


def generate_mandelbrot_images():
    global width, height, saturation, value
    width, height = 1920, 1080
    real_start, real_end = -2, 1
    imaginary_start, imaginary_end = -1, 1
    saturation = 255
    # create image objects
    bw_image = Image.new("RGB", (width, height), (0, 0, 0))
    color_image = Image.new("HSV", (width, height))
    # create drawing objects
    bw_draw = ImageDraw.Draw(bw_image)
    color_draw = ImageDraw.Draw(color_image)
    for x, y in itertools.product(range(width), range(height)):
        # convert pixel coordinates to complex coordinates
        c = complex(
            real_start + (x / width) * (real_end - real_start),
            imaginary_start + (y / height) * (imaginary_end - imaginary_start),
        )
        # compute the number of iterations
        iterations = generate_mandelbrot(c)
        # determine the color of the points
        black_and_white = hue = int(iterations * 255 / max_iterations)
        value = 255 if iterations < max_iterations else 0
        # plot the points
        # black and white image
        bw_draw.point([x, y], (black_and_white, black_and_white, black_and_white))
        # color image
        color_draw.point([x, y], (hue, saturation, value))
    bw_image.save("mandelbrot_black_and_white.png", "PNG")
    color_image.convert("RGB").save("mandelbrot_color.png", "PNG")
