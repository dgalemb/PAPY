import numpy as np
from PIL import Image
from numba import jit
from time import time

from mandelbrot import mandelbrot, is_in_Mandelbrot, is_in_mandelbrot_numba, mandelbrot_set, plot_mandelbrot
from julia import julia, is_in_Julia, is_in_julia_numba, julia_set, plot_julia


np.warnings.filterwarnings("ignore")


# Argsparse code here

if __name__=="__main__":
    start_time = time()
    # mandelbrot_image(zmin=-2-1.2j, zmax=0.5+1.2j, pixel_size=5e-4, max_iter=100, figname="Mandelbrot.png")
    plot_mandelbrot()
    elapsed_time = time() - start_time
    print(f"mandelbrot: {elapsed_time} seconds.")

    start_time2 = time()
    plot_julia()
    elapsed_time2 = time() - start_time2
    print(f"julia: {elapsed_time2} seconds.")
