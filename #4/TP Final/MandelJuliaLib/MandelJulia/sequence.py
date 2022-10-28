import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))


def sequence(c, z=0):
    """
    Defining generic generator objet

    Parameters
    ----------
    c : complex
        parameter c of the Mandelbrot/Julia sequence
    z : complex
        beginning of the Mandelbrot/Julia sequence (default is 0)

    Returns
    -------
    z : complex
        possible Mandelbrot/Julia sequence number.
    """
    while True:
        yield z
        z = z * 2 + c
