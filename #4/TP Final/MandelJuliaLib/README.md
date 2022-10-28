# Introduction

Library that enables the visualization of the Mandelbrot and Julia series, as well as checking if certain constance values belong to each one of the sets.

For a referece of what they are, their mathematical definitons and properties please check [Mandelbrot](https://en.wikipedia.org/wiki/Mandelbrot_set) and [Julia](https://en.wikipedia.org/wiki/Julia_set).

# Installing and Importing

To install it, download the folder (or clone the repository), set your path to its location and install it with pip (or pip3): pip install .

Then, to import the functions described below the following command must be made inside Python:

```
from MandelJulia import functions
```

And so, we can use the functions simply with `functions.name_of_the_function`. For instance `functions.is_in_Mandelbrot(0.25)`.

If only one - or a few - of the functions are wished to be used, we can make a more direct import:

```
from MandelJulia.functions import is_in_Mandelbrot
```

And, use the function directly: `is_in_Mandelbrot(0.25)`

# Argspace usage

On the top of importing the functions to usage them directly in a Python script we can obtain the plots directly from the terminal with:

```
python /path/to/MandelJulia/functions.py MandelbrotPlot -o mandelbrot.png

python /path/to/MandelJulia/functions.py JuliaPlot -o julia.png
```

***Please note***: The path here is to MandelJulia, not to MandelJuliaLib (the downloaded folder), the relative path between them is: MandelJuliaLib/MandelJulia.

The commands shown produce the default images but we can change the parameters as we wish, for instance:

```
python /path/to/MandelJulia/functions.py MandelbrotPlot 
                            --zmin=-0.7440+0.1305j\
                            --zmax=-0.7425+0.1320j\
                            --pixel_size=5e-7\
                            --max-iter=50\
                            -o "Mandelbrot_tentacle_lowiter.png"

python /path/to/MandelJulia/functions.py JuliaPlot 
                            --c=-0.8j\
                            --pixel_size=1e-3\
                            --max-iter=50\
                            -o "thunder-julia.png"
```

# Functions

There are 4 functions in the library: 

- In set functions
    - `is_in_Mandelbrot` that checks if a certain constant belongs to the respective set
    - `is_in_Julia` that checks if a certain constant (in regards to the given `z_0`) belongs to the respective set

- Plot functions
    - `plot_mandelbrot` plots the Mandelbrot set for a given range in the complex plane, the constant c, pixel size and number of iterations
    - `plot_julia` plots the Julia set for a given range in the complex plane, an starting `z_0`, the constant c, pixel size and number of iterations

Note that default values are defined for each function, so even a default image can be plotted if no argument is given.

The code was optimized with the Numba library, but, even then, it may take too much time to finish the plots if the pixel size given is too small in regards to the size of the complex plane chosen and/or the max iterations given.

