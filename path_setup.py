import os
import sys

#Get the frame folder and add it to the main code path
def add_frames_path(File="Frames_Code"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    frames_dir = os.path.join(current_dir, File)
    if frames_dir not in sys.path:
        sys.path.append(frames_dir)

#this one is similar but the different is that this gets the file 
def get_data_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'Data_Side', filename)
