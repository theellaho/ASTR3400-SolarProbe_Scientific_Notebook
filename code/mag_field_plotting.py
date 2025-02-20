## Ella Ho
## University of Colorado at Boulder
## ASTR 3400 - Research Methods
## v01 // 2025-02-12 // Creating a magnetic field plotting function.

# This code produces a plot from magnetic field data.

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

## Import tools to convert time.
from datetime import datetime, timedelta


#########################################
##### Magnetic Field Plot
#########################################

def magFieldPlot (path, file, datetime1, datetime2): 
    
    ## Opening file.
    tvars = cdf_to_tplot(path+file, get_support_data=1)
    
    ## Get the data in useful arrays.
    atemp = get_data('psp_fld_l2_mag_SC_4_Sa_per_Cyc')
    epoch_mag_sc = atemp[0] # Fluxgate Magnetometer Data
    data_mag_sc = atemp[1] # Time Data
    
    ## Converts time data from epoch time to UTC.
    time = [datetime.utcfromtimestamp(t) for t in epoch_mag_sc]
    
    ## Defining 20 minute interval.
    start_time = datetime1
    end_time = datetime2
    mask = (np.array(time) >= start_time) & (np.array(time) <= end_time)
    
    ## Extracting data during the given time interval. 
    time_interval = np.array(time)[mask]
    mag_interval = data_mag_sc[mask]
    
    ## Extracting data for each mag field comp during the given time interval.
    bx = mag_interval[:,0] 
    by = mag_interval[:,1] 
    bz = mag_interval[:,2] 
    
    ## Calculating magnitude.
    magnitude = np.sqrt(bx**2 + by**2 +bz**2)
    
    ## Creates a plot object.
    fig, ax = plt.subplots()
    
    ## Set the font size (global).
    fs = 12
    plt.rcParams['font.size'] = str(fs)
    
    ## Set tick font size.
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontsize(fs)
    
    ## Plotting the data. 
    plt.plot(time_interval, bx, label = "Magnetic Field (X-Component)")
    plt.plot(time_interval, by, label = "Magnetic Field (Y-Component)")
    plt.plot(time_interval, bz, label = "Magnetic Field (Z-Component)")
    plt.plot(time_interval, magnitude, label = "Magnitude of the Magnetic Field")
    
    ## Adding Labels.
    ax.set_xlabel('Time (UTC)', fontsize = fs) # X-axis
    ax.set_ylabel('Magnetic Field (nT)', fontsize = fs) #Y-axis
    ax.set_title("Fluxgate Magnetometer", fontsize = fs) #Title
    
    ## Adding a Key.
    leg = ax.legend(bbox_to_anchor=(1.01, 1), loc="upper left", borderaxespad=0.)
    
    ## Stop operating on this plot.
    plt.show()