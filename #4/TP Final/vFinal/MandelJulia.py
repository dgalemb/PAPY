import matplotlib.pyplot as plot
import numpy as np
from PIL import Image
from numba import jit
from time import time


np.warnings.filterwarnings("ignore")

def sequence(c, z = 0):
    '''Defining generic generator objet '''
    while True:
        yield z
        z = z * 2 + c

def mandelbrot(candidate):
    '''Defining the generator to Mandelbrot sequence (z = 0, c given)'''
    return sequence(z = 0, c = candidate)

def julia(candidate, parameter):
    '''Defining the generator to Julia sequence (z and c given)'''
    return sequence(z = candidate, c = parameter)

def is_in_Mandelbrot(c, max_iter = 100):
    '''
    Defining funcion to check if wheter the Mandelbrot sequence converges for a given c and max_iter
    Once z 'gets out' of the disc centered @ (0,0) with radius = 2, the series will diverge and then we stop the function
    More iterations yield more precise results, specially for c's in the border
    The default value for max_iter is 100, which generally is sufficient for most values of c
    '''
    z = 0
    for _ in range(max_iter):
        z = z ** 2 + c
    return abs(z) <= 2


def is_in_Julia(z0, c, max_iter = 100):
    ''''
    Defining funcion to check if wheter the Julia sequence converges for a given c, z0 and max_iter
    The same observations from is_in_Mandelbrot are valid
    Note that is_in_Julia can be equivalent to is_in_Mandelbrot <==> z0 = 0
    '''
    z = z0
    for _ in range(max_iter):
        z = z ** 2 + c
    return abs(z) <= 2

def complex_matrix(x_min, x_max, y_min, y_max, pixel_size):
    ''''
    Function that creates the 2d array of points (values of c) in the complex plane based on maximum and minimum coordinates
    These points are the values of c that are going to be used to be evaluated with is_in_Set functions to create the graphs
    Pixel size is the desired distance between the points
    '''
    re1 = np.arange(x_min, x_max, pixel_size)
    im1 = np.arange(y_min, y_max, pixel_size)
    return re1[np.newaxis, :] + im1[:, np.newaxis] * 1j

def plot_mandelbrot(zmin=-2-1.2j, zmax=0.5+1.2j, pixel_size=5e-4, max_iter=50, figname='Mandelbrot.png'):
    c = complex_matrix(zmin.real, zmax.real, zmin.imag, zmax.imag, pixel_size=pixel_size)
    data = ~is_in_Mandelbrot(c, max_iter=max_iter)
    image = Image.fromarray(data)
    image.save(figname)

from timeit import default_timer as timer
start = timer()
plot_mandelbrot(zmin=-2-1.2j, zmax=0.5+1.2j, pixel_size=5e-4, max_iter=50, figname="Mandelbrot_Base.png")
end = timer()
print(end - start)



# Test Mandelbrot : default
start_time = time()
plot_mandelbrot()
elapsed_time = time() - start_time
print(f"mandelbrot: {elapsed_time} seconds.")

# Test Julia : default
start_time2 = time()
plot_julia()
elapsed_time2 = time() - start_time2
print(f"julia: {elapsed_time2} seconds.")
