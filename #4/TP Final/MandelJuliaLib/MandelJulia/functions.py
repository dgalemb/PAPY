import argparse
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))

from mandelbrot import mandelbrot, is_in_Mandelbrot, is_in_mandelbrot_numba, mandelbrot_set, plot_mandelbrot
from julia import julia, is_in_Julia, is_in_julia_numba, julia_set,  plot_julia

"""
Mandelbrot and Julia Fractals

Use the MandelbrotPlot and/or JuliaPlot expressions on the command line to test their use.
"""

parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest="function")

mandelbrot_subparser = subparser.add_parser("MandelbrotPlot", help="Plots a Mandelbrot fractal")
mandelbrot_subparser.add_argument("--zmin", type=str, default="-2-1.2j", help="Coordinate of the lower left corner of "
                                                                              "the fractal section to print. Write as"
                                                                              " a complex number")
mandelbrot_subparser.add_argument("--zmax", type=str, default="0.5+1.2j", help="Coordinate of the upper right corner "
                                                                               "of the fractal section to print. "
                                                                               "Write as a complex number")
mandelbrot_subparser.add_argument("--pixel_size", type=float, default=5e-4, help="Size of each pixel of the image; "
                                                                                 "space between the minimum and "
                                                                                 "maximum coordinate values.")
mandelbrot_subparser.add_argument("--max_iter", type=int, default=50, help="Number of iterations for the sequence")
mandelbrot_subparser.add_argument("-o", type=str, default="Mandelbrot.png", help="Name of the image to be created")

julia_subparser = subparser.add_parser("JuliaPlot", help="Plots a Julia fractal")
julia_subparser.add_argument("-c", type=str, default="-0.8j", help="Parameter c of the Julia sequence")
julia_subparser.add_argument("--zmin", type=str, default="-2-1.5j", help="Coordinate of the lower left corner of the "
                                                                         "fractal section to print. Write as a "
                                                                         "complex number")
julia_subparser.add_argument("--zmax", type=str, default="2+1.5j", help="Coordinate of the upper right corner of the "
                                                                        "fractal section to print. Write as a complex"
                                                                        " number")
julia_subparser.add_argument("--pixel_size", type=float, default=1e-3, help="Size of each pixel of the image; space "
                                                                            "between the minimum and maximum "
                                                                            "coordinate values.")
julia_subparser.add_argument("--max_iter", type=int, default=50, help="Number of iterations for the sequence")
julia_subparser.add_argument("-o", type=str, default="Julia.png", help="Name of the image to be created")

args = parser.parse_args()


if __name__ == "__main__":
    if args.function == 'MandelbrotPlot':
        z_min_complex = complex(args.zmin.replace(" ", ""))
        z_max_complex = complex(args.zmax.replace(" ", ""))
        plot_mandelbrot(z_min_complex, z_max_complex, args.pixel_size, args.max_iter, args.o)

    if args.function == 'JuliaPlot':
        c_complex = complex(args.c.replace(" ", ""))
        z_min_complex = complex(args.zmin.replace(" ", ""))
        z_max_complex = complex(args.zmax.replace(" ", ""))
        plot_julia(c_complex, z_min_complex, z_max_complex, args.pixel_size, args.max_iter, args.o)
