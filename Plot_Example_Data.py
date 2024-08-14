"""
Author: Sarah Tennant
Date: 21/6/2024
Script: Plot_Example_Data.py

Description: This script loads a single recording file and makes a 10 second plot with 4 channels of EEG data.

"""

import sys
import os.path
import numpy as np
from numpy import *
import os
import matplotlib.pyplot as plt
import mne
import pandas as pd
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar

import parameters # this is a script to import


prm = parameters.Parameters()


# set global parameters
def parameters():
    prm.set_sampling_rate(250.4)
    prm.set_number_of_channels(16)
    prm.set_sample_datatype('int16')
    prm.set_display_decimation(1)


def process_dir(file_name):
    # Load the raw (1-D) data
    dat_raw = np.fromfile(file_name, dtype=prm.get_sample_datatype())

    # Reshape the (2-D) per channel data
    step = prm.get_number_of_channels() * prm.get_display_decimation()
    dat_chans = [dat_raw[c::step] for c in range(prm.get_number_of_channels())]

    # Build the time array
    data=np.array(dat_chans)

    del(dat_chans)
    channel_names=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    channel_types=['emg','misc','eeg','misc','misc','misc','emg','misc','misc','misc','misc','misc','eeg','misc','misc','eeg']

    # This creates the info that goes with the channels, which is names, sampling rate, and channel types
    info = mne.create_info(channel_names, prm.get_sampling_rate(), channel_types)

    # This makes the object that contains all the data and info about the channels. Computations like plotting, averaging, power spectrums can be performed on this object
    custom_raw = mne.io.RawArray(data, info)
    return custom_raw


def crop_by_start_and_end(custom_raw):
    print('Cropping recording based on start and end times....')

    # Enter the start and end times of a 6-10 second part of the recording you want to plot as example data
    cropped_raw = custom_raw.crop(tmin=139947, tmax=139952) # crop up to 10 seconds for example plotting
    return cropped_raw


def normalise_eeg_data(eeg_data, eeg_channel):
    channel_data = eeg_data.iloc[:,eeg_channel]
    mean_of_channel = np.mean(channel_data)
    channel_normalised = channel_data - mean_of_channel
    return channel_normalised


def plot_example(output_figure_path, first_eeg, second_eeg, third_eeg, fourth_eeg, time):

    eeg = plt.figure(figsize=(16, 12))
    ax = eeg.add_subplot(4, 1, 1)  # specify (nrows, ncols, axnum
    ax.plot(time,first_eeg, color='Black', markersize=2.5)
    plt.ylabel(u"\u03bcV", fontsize=18, labelpad=10)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(-150, 150)
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom=False,  # ticks along the bottom edge are off
        labelbottom=False, # labels along the bottom edge are off
        labelsize=16,length=5,width=1.5)
    plt.tick_params(
        axis='y',  # changes apply to the y-axis
        which='both', right=False,left=True,labelleft=True,labelsize=16,length=5,width=1.5)


    ax = eeg.add_subplot(4, 1, 2)  # specify (nrows, ncols, axnum
    ax.plot(time,second_eeg, color='Black', markersize=2.5)
    plt.ylabel(u"\u03bcV", fontsize=18, labelpad=10)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(-150, 150)
    plt.tick_params(axis='x', which='both', bottom=False,labelbottom=False,labelsize=16,length=5,width=1.5)
    plt.tick_params(axis='y',which='both',right=False,left=True,labelleft=True,labelsize=16,length=5,width=1.5)

    ax = eeg.add_subplot(4, 1, 3)  # specify (nrows, ncols, axnum
    ax.plot(time,third_eeg, color='Black', markersize=2.5)
    plt.ylabel(u"\u03bcV", fontsize=18, labelpad=10)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(-150, 150)
    plt.tick_params(axis='x', which='both', bottom=False,labelbottom=False,labelsize=16,length=5,width=1.5)
    plt.tick_params(axis='y',which='both',right=False,left=True,labelleft=True,labelsize=16,length=5,width=1.5)

    ax = eeg.add_subplot(4, 1, 4)  # specify (nrows, ncols, axnum
    ax.plot(time,fourth_eeg, color='Black', markersize=2.5)
    plt.ylabel(u"\u03bcV", fontsize=18, labelpad=10)
    plt.xlabel('Time (seconds)', fontsize=18, labelpad=15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(-150, 150)
    plt.tick_params(axis='x', which='both', bottom=True,labelbottom=True,labelsize=16,length=5,width=1.5)
    plt.tick_params(axis='y',which='both',right=False,left=True,labelleft=True,labelsize=16,length=5,width=1.5)

    plt.subplots_adjust(hspace=.35, wspace=.35, bottom=0.15, left=0.1, right=0.9, top=0.9)
    plt.savefig(output_figure_path + '/' + 'ExampleTrace_0100.png', dpi=200)
    plt.close()




def main():
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')

    #path to the recording .dat file
    recording_folder = '/Volumes/Sarah/SYNGAPE8/DATA/SYNGAPE8/12W/SYNGAPE8_2780/TAINI_1048_2780_EM4-2024_04_05-0000.dat'
    output_figure_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_2780/'

    print("I am plotting example figure for " + str(recording_folder))

    # set eeg channels to plot
    eeg_channels = [5, 8, 9, 10] # change these to the channels you want to plot

    # SET PARAMETERS
    parameters()

    # LOAD DATA
    eeg_data = process_dir(recording_folder) # overall data

    # CROP DATA
    cropped_eeg = crop_by_start_and_end(eeg_data)

    # REDISTRIBUTE EEG SIGNAL AROUND 0 FOR PLOTTING
    eeg_data = cropped_eeg.to_data_frame() # convert data from mne object to pandas dataframe
    first_eeg = normalise_eeg_data(eeg_data, eeg_channels[0]) # normalise the first eeg channel around 0
    second_eeg = normalise_eeg_data(eeg_data, eeg_channels[1]) # normalise the second eeg channel around 0
    third_eeg = normalise_eeg_data(eeg_data, eeg_channels[2]) # normalise the third eeg channel around 0
    fourth_eeg = normalise_eeg_data(eeg_data, eeg_channels[3]) # normalise the fourth eeg channel around 0

    # CREATE TIME ARRAY FOR PLOTTING
    eeg_data['time'] = eeg_data.index/250.4

    # PLOT EXAMPLE DATA
    plot_example(output_figure_path, first_eeg, second_eeg, third_eeg, fourth_eeg, np.array(eeg_data.loc[:,"time"]))



if __name__ == '__main__':
    main()

