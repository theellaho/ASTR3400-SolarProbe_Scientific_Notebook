## Ella Ho
## University of Colorado at Boulder
## ASTR 3400 - Research Methods
## v01 // 2025-02-12 // Creating a Sine Function.

# This code produces a sine wave from given data. 

#########################################
##### Import Section
#########################################

## General Math and Plotting Imports.
import matplptlib.pyplot as plt
import numpy as np

## For Reading CDFs
import cdflib

## Import scripts from pytplot
from pytplot import cdf_to+tplot
from pytplot import get_data

## import scriptions from PySpedas
import pyspedas
from pyspedas import time_double
from pyspedas import time_string


#########################################
##### Basic 2D Line Plot
#########################################

def sinewaveplot (line_plot_2d_data_x, line_plot_2d_data_y):
    ## Creates a plot object.
    fig, ax = plt.subplots()
    
    ## Set the font size (global).
    fs = 12
    plt.rcParams['font.size'] = str(fs)
    
    # Set tick font size.
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontsize(fs)
    
    ## Plot the raw data points. 
    ax.scatter(line_plot_2d_data_x, line_plot_2d_data_y, color = 'blue', label = "data", s = 30.0)
    
    # Label the x axis.
    ax.set_xlabel('Degrees', fontsize = fs)
    
    # Label the y axis.
    ax.set_ylabel('Amplitude', fontsize = fs)
    
    # Create a title.
    ax.set_title("A sine wave", fontsize = fs)
    
    ## Plot the line that connects the data points
    ax.plot(line_plot_2d_data_x, line_plot_2d_data_y, color = 'red', label = "A line")
    
    ## Add a key.
    leg = ax.legend(bbox_to_anchor=(1.01, 1), loc="upper left", borderaxespad=0.)
    
    ## Stop operating on this plot
    plt.show()