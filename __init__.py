"""
gfc: a module for processing and interpreting data from ESA's Gaia satellite, with a particular focus on the extreme deconvolution (XD) algorithm.

Submodules:

gfc.tgas
    Functions specific to the TGAS dataset
gfc.pdf
    Functions for dealing with probability density functions (PDFs)
gfc.io
    Functions for input and output, to file and to screen
gfc.mapping
    Functions for mapping other functions over large datasets, using multiprocessing and numpy magic where possible
gfc.gplot
    Functions for easily making plots that one is likely to make many times
gfc.general:
    General functions and constants; these are all imported directly into gfc
"""
from gfc import *
