import os
import cv2
#from utils import get_area, plot_area_distribution
from data_loader import DataLoader



dl = DataLoader()
img_path_list, label_path_list = dl.get_path_list()
num_empty = 0
# Look for empty label files
for img_path, lbl_path in zip(img_path_list, label_path_list):

    # Read the label file
    with open(lbl_path, 'r') as f:
        # read first character
        first_char = f.read(1)

        if not first_char:
            num_empty += 1
            
print(f"Number of empty labels: {num_empty}\nTotal labels: {len(label_path_list)}")
    