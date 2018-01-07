'''
Helper functions for Jupyter notebooks. This code is not from the book.
'''
import sys, os
import matplotlib.pyplot as plt

# This is Needed for importing our linear algebra and other functions.
sys.path.append(os.path.join('..','code-python3'))

def double_x_size():
    '''Return the size of the current figure with the doubled X size.
       Used to set the size of the figure for two plots.'''
    return plt.gcf().get_size_inches() * (2, 1)

def double_y_size():
    '''Return the size of the current figure with the doubled Y size.
       Used to set the size of the figure for two plots.'''
    return plt.gcf().get_size_inches() * (1, 2)

def double_xy_size():
    '''Return the size of the current figure with the doubled X and Y size.
       Used to set the size of the figure for two plots.'''
    return plt.gcf().get_size_inches() * (2, 2)
