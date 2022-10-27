from setuptools import setup

setup(
    name='MandelJulia',
    version='0.1.0',
    description='Library to visualize and Mandelbrot and Julia sets',
    packages=['MandelJulia'],
    author='dgalemb, nucontreras',
    license='MIT',
    Install_requires = ['numpy', 'time', 'numba', 'PIL', 'argspace'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)