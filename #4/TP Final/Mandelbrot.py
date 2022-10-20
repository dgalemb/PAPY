import numpy as np
import itertools as it
import matplotlib.pyplot as plot  
import time


class MandelJulia:

    def __init__(self):
        pass

    def calculat(self, n, c, computed = {0: complex(0,0)}):
        if n not in computed:
            computed[n] = self.calculat(n-1, c, computed)**2 + complex(c,0)
        return computed[n]

    def in_set(self, c, z = complex(0,0), max_iter = 10):
        for k in np.arange(max_iter):
            if abs(self.calculat(k, c, computed = {0: z})) > 2:
                return False

        return True

    def plot(self, z = complex(0,0), z_min = complex(-2,0), z_max = complex(2,0), pixel_size = 3, max_iter = 10):
        x_min = z_min.real
        x_max = z_max.real

        xstep = np.linspace(x_min, x_max, pixel_size)
        ystep = np.linspace(x_min, x_max, pixel_size)

     
        grid = xstep[:, None] + 1j*ystep
 
        grid = np.array(list(it.chain.from_iterable(grid)))
    
        mask = [self.in_set(k, z, max_iter) for k in grid]


        true_grid = np.array(grid)[mask]
        reals = [k.real for k in true_grid]
        imags = [k.imag for k in true_grid]
        
        plot.scatter(reals, imags, color = "Red", marker = ",", s = 1)  
        plot.gca().set_aspect("equal")  
        plot.axis("off")  
        plot.tight_layout()  
        plot.show()  



def is_in_Julia(z, c, max_iter = 500):

    jullie = MandelJulia()
    return jullie.in_set(c, z, max_iter)

def is_in_Mandelbrot(c, max_iter = 500):

    mand = MandelJulia()
    return mand.in_set(c, max_iter)

mand = MandelJulia()
print(mand.plot(pixel_size=1000, c = complex(0, -0.8), max_iter=50))
