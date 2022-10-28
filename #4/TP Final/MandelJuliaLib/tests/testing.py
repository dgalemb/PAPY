from MandelJulia.mandelbrot import mandelbrot, is_in_Mandelbrot, is_in_mandelbrot_numba, mandelbrot_set, plot_mandelbrot
from MandelJulia.julia import julia, is_in_Julia, is_in_julia_numba, julia_set, plot_julia


def test_inMandelbrot():

    assert mandelbrot.is_in_Mandelbrot(c=0.251) == True

def test_inJulia():

    assert julia.is_in_julia(z0=0.25+0.25j, c=0.25) == True