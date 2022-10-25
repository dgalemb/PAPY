import numpy as np
from PIL import Image
from numba import jit

from sequence import sequence


np.warnings.filterwarnings("ignore")


def mandelbrot(candidate):
    """
    Defining the generator to Mandelbrot sequence (z = 0, c given)

    Parameters
    ----------
    candidate : complex
        parameter c of the Mandelbrot sequence

    Returns
    -------
    generator
        a Mandelbrot sequence generator
    """
    return sequence(z=0, c=candidate)


def is_in_Mandelbrot(c, max_iter=100):
    """
    Defining funcion to check if wheter the Mandelbrot sequence converges for a given c and max_iter
    Once z 'gets out' of the disc centered @ (0,0) with radius = 2, the series will diverge, and then
    we stop the function
    More iterations yield more precise results, specially for c's in the border
    The default value for max_iter is 100, which generally is sufficient for most values of c

    Parameters
    ----------
    c : complex
        parameter c of the Mandelbrot sequence
    max_iter : int
        number of iterations for the sequence

    Returns
    -------
    bool
        Returns True if the calculated z value belongs to the sequence.
    """
    z = 0
    for _ in range(max_iter):
        z = z ** 2 + c
    return abs(z) <= 2


@jit
def is_in_mandelbrot_numba(creal, cimag, maxiter):
    """
    Modification of the is_in_Mandelbrot function for iterative use in conjunction with the numba package.
    The complex number has been previously decomposed into its real and imaginary part.
    Once z "exits" the disk centered at (0,0) with radius = 2, the series diverges and the function returns True.
    If the series does not diverge the function returns False.
    True is returned when the series diverges in order to save the photo immediately with the pillow package,
    without having to invert the colors black and white

    Parameters
    ----------
    creal : float
        The file location of the spreadsheet
    cimag : float
        The file location of the spreadsheet
    maxiter : int
        number of iterations for the sequence

    Returns
    -------
    bool
        Returns True if the calculated z value does not belong to the sequence.
        False in another case.
    """
    real = creal
    imag = cimag
    for n in range(maxiter):
        real2 = real * real
        imag2 = imag * imag
        if real2 + imag2 > 4.0:
            return True
        imag = 2 * real * imag + cimag
        real = real2 - imag2 + creal
    return False


@jit
def mandelbrot_set(x_min, x_max, y_min, y_max, pixel_size, max_iter):
    """
    Function that creates a Boolean array with the points that belong (False) and do not belong (True)
    to the Mandelbrot set.
    The matrix is created iteratively, taking into account the list r1 with the real values and another
    list r2 with the imaginary values.
    Use the jit function of the numba package to speed up the processing.

    Parameters
    ----------
    x_min : float
        minimum value of the x-coordinate
    x_max : float
        maximum value of the x-coordinate
    y_min : float
        minimum value of the y-coordinate
    y_max : float
        maximum value of the y-coordinate
    pixel_size : float
        size of each pixel of the image; space between the minimum and maximum coordinate values.
    max_iter : int
        number of iterations for the sequence

    Returns
    -------
    numpy.ndarray
        Boolean matrix with the fractal information
    """
    r1 = np.arange(x_min, x_max, pixel_size)
    r2 = np.arange(y_min, y_max, pixel_size)
    width = len(r1)
    height = len(r2)
    n3 = np.empty((width, height), dtype=bool)
    for i in range(width):
        for j in range(height):
            n3[i, j] = is_in_mandelbrot_numba(r1[i], r2[j], max_iter)
    return n3


def plot_mandelbrot(zmin=-2-1.2j, zmax=0.5+1.2j, pixel_size=5e-4, max_iter=50, figname='Mandelbrot.png'):
    """
    Function that creates and saves an image of the Mandelbrot fractal.
    It uses the Image method of the PIL package for image processing.
    The Boolean matrix obtained must be transposed (z.T) due to the way its data is calculated.
    The default values are strategically given in order to display most of the values that belong to the set.

    Parameters
    ----------
    zmin : complex
        coordinate of the lower left corner of the fractal section to print.
        It belongs to the complex plane.
    zmax : complex
        coordinate of the upper right corner of the fractal section to print.
        It belongs to the complex plane.
    pixel_size : float
        size of each pixel of the image; space between the minimum and maximum coordinate values.
    max_iter : int
        number of iterations for the sequence
    figname : str
        name of the image to be created

    Returns
    -------
    None
    """
    z = mandelbrot_set(zmin.real, zmax.real, zmin.imag, zmax.imag, pixel_size=pixel_size, max_iter=max_iter)
    image = Image.fromarray(z.T)
    image.save(figname)
