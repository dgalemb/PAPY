Library that enables the visualization of the Mandelbrot and Julia series, as well as checking if certain constance values belong to each one of the sets.

To install it, download the folder, set your path to its location and install it with pip (or pip3): pip install.

There are 4 functions to the library: 

- is_in_Mandelbrot, is_in_Julia that check if a certain constant belongs to the respective set and plot_mandelbrot

- plot_julia that plot the set for a given range, pixel size and number of iterations. 
Note that default values are defined for each function, so even a default image can be plotted if no argument is given.
The code was optimized with the Numba library, but, even then, it may take too much time to finish the plots if the pixel size given is too small in regards to the size of the complex plane chosen and/or the max iterations given.

