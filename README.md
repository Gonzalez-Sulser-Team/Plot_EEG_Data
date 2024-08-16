## Plotting example snippets of EEG data


This script loads a single recording file using the MNE package (v1.6.1) in python (v3.12) and plots a 5-10 second snippet of data from 4 selected channels using Matplotlib (v3.8.3). The output of the script should appear as the figure below saved as a .png into the output folder specified in the script. 

### Output file: 

![ExampleTrace_0100](https://github.com/user-attachments/assets/ee479b18-7b87-4f51-a698-dc8f0b3f89f3)





### Instructions:

Navigate to the main function and enter the recording file you want to use in the recording_folder parameter  

```ruby
recording_folder = '/Volumes/Sarah/SYNGAPE8/DATA/SYNGAPE8/12W/SYNGAPE8_2780/TAINI_1048_2780_EM4-2024_04_05-0000.dat'
```

Edit the output path to the desired folder you want to save the output figure into 

```ruby
output_figure_path = '/Volumes/Sarah/SYNGAPE8/OUTPUT/SYNGAPE8/12W/SYNGAPE8_2780/'
```

Enter the EEG channels you want to plot in eeg_channels parameter

```ruby
eeg_channels = [5, 8, 9, 10] # change these to the channels you want to plot
```

Navigate to the crop_by_start_and_end function and enter the start and end time in seconds of the snippet of EEG data you want to plot. tmin is the start or minimum time and tmax is the end of max time.

```ruby
cropped_raw = custom_raw.crop(tmin=137943, tmax=137947) # crop up to 10 seconds for example plotting
```
