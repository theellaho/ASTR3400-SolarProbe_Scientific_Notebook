## Ella Ho
## University of Colorado at Boulder
## ASTR 3400 - Research Methods
## v01 // 2025-02-12 // Creating a orbital plotting function.

# This code produces a plot from the PSP orbital data.

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

def orbitalPlot (path, file, datetime1, datetime2): 
    
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

    ## Extracting x, y, and z positions for the Parker Space Probe's recorded trek.
    position_x = position[:,0]
    position_y = position[:,1]
    position_z = position[:,2]

    ## Calculate an encounter's [x,y,z] positions and times. 
    first_event = time_double(datetime1) # Convert to UNIX timestamp.
    second_event = time_double(datetime2) # Convert to UNIX timestamp.

    ## Masking the data to filter the time range for just given encounter.
    mask = (epoch >= first_event) & (epoch <= second_event) 

    ## Defining x, y, and time for the encounter. 
    encounter_x = position_x[mask]
    encounter_y = position_y[mask]
    encounter_z = position_z[mask]
    encounter_time = epoch[mask]

    ## Creates a plot object.
    fig, ax = plt.subplots()
    
    ## Set the font size (global).
    fs = 12
    plt.rcParams['font.size'] = str(fs)
    
    ## Set tick font size.
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontsize(fs)
    
    ## Plotting the data. 
    plt.plot(encounter_x, encounter_y, label = "Encounter 18", color='purple', linewidth=2, linestyle="--")
    
    ## Adding Labels.
    ax.set_xlabel('X-Component', fontsize = fs) # X-axis
    ax.set_ylabel('Y-Component', fontsize = fs) #Y-axis
    ax.set_title("X and Y Position of Encounter", fontsize = fs) #Title
    
    ## Adding a Key.
    leg = ax.legend(bbox_to_anchor=(1.01, 1), loc="upper left", borderaxespad=0.)
    
    ## Stop operating on this plot.
    plt.show()