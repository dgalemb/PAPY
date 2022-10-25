import numpy as np
from PIL import Image
from numba import jit

from sequence import sequence


np.warnings.filterwarnings("ignore")


def julia(candidate, parameter):
    """
    Defining the generator to Julia sequence (z and c given)

    Parameters
    ----------
    candidate : complex
        parameter z of the Julia sequence
    parameter : complex
        parameter c of the Julia sequence

    Returns
    -------
    generator
        a Julia sequence generator
    """
    return sequence(z=candidate, c=parameter)


def is_in_Julia(z0, c, max_iter=100):
    """
    Defining function to check if wheter the Julia sequence converges for a given c, z0 and max_iter
    The same observations from is_in_Julia are valid
    Note that is_in_Julia can be equivalent to is_in_Julia <==> z0 = 0

    Parameters
    ----------
    z0 : complex
        beginning of the Julia sequence
    c : complex
        parameter c of the Julia sequence
    max_iter : int
        number of iterations for the sequence

    Returns
    -------
    bool
        Returns True if the calculated z value belongs to the sequence.
    """
    z = z0
    for _ in range(max_iter):
        z = z ** 2 + c
    return abs(z) <= 2


@jit
def is_in_julia_numba(zreal, zimag, c, maxiter):
    """
    Modification of the is_in_Julia function for iterative use in conjunction with the numba package.
    The complex number has been previously decomposed into its real and imaginary part.
    Once z "exits" the disk centered at (0,0) with radius = 2, the series diverges and the function returns True.
    If the series does not diverge the function returns False.
    True is returned when the series diverges in order to save the photo immediately with the pillow package,
    without having to invert the colors black and white.

    Parameters
    ----------
    zreal : float
        real part of the complex number z of the Julia sequence.
    zimag : float
        imaginary part of the complex number z of the Julia sequence.
    c : complex
        parameter c of the Julia sequence
    maxiter : int
        number of iterations for the sequence

    Returns
    -------
    bool
        Returns True if the calculated z value does not belong to the sequence.
        False in another case.
    """
    real = zreal
    imag = zimag
    creal = c.real
    cimag = c.imag
    for n in range(maxiter):
        real2 = real * real
        imag2 = imag * imag
        if real2 + imag2 > 4.0:
            return True
        imag = 2 * real * imag + cimag
        real = real2 - imag2 + creal
    return False


@jit
def julia_set(c, x_min, x_max, y_min, y_max, pixel_size, max_iter):
    """
    Function that creates a Boolean array with the points that belong (False) and do not belong (True)
    to the Julia set.
    The matrix is created iteratively, taking into account the list r1 with the real values and another
    list r2 with the imaginary values.
    Use the jit function of the numba package to speed up the processing.

    Parameters
    ----------
    c : complex
        parameter c of the Julia sequence
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
            n3[i, j] = is_in_julia_numba(r1[i], r2[j], c, max_iter)
    return n3


def plot_julia(c=-0.8j, zmin=-2-1.5j, zmax=2+1.5j, pixel_size=1e-3, max_iter=50, figname="Julia.png"):
    """
    Function that creates and saves an image of the Julia fractal.
    It uses the Image method of the PIL package for image processing.
    The Boolean matrix obtained must be transposed (z.T) due to the way its data is calculated.
    The default values are strategically given in order to display most of the values that belong to the set.

    Parameters
    ----------
    c : complex
        parameter c of the Julia sequence
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
    z = julia_set(c, zmin.real, zmax.real, zmin.imag, zmax.imag, pixel_size=pixel_size, max_iter=max_iter)
    image = Image.fromarray(z.T)
    image.save(figname)
