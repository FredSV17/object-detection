import os
import cv2
#from utils import get_area, plot_area_distribution
from data_loader import DataLoader
import matplotlib.pyplot as plt

from utils import show_bboxes



# Look for empty label files
def check_for_empty_label_files(train_labels, test_labels,save_results=True):
    num_empty_train = 0
    num_empty_test = 0
    for lbl_train, lbl_test in zip(train_labels, test_labels):

        # Read the label file (train)
        with open(lbl_train, 'r') as f:
            # read first character
            first_char = f.read(1)

            if not first_char:
                num_empty_train += 1
        f.close()
        
        # Read the label file (test)    
        with open(lbl_test, 'r') as f:
            # read first character
            first_char = f.read(1)

            if not first_char:
                num_empty_test += 1
        f.close()
    train_report_str = f"Number of empty labels (train): {num_empty_train}\
        \nTotal labels: {len(train_labels)}\
        \nPercentage: {num_empty_train*100/len(train_labels)}"
    test_report_str = f"Number of empty labels (test): {num_empty_test}\
        \nTotal labels: {len(test_labels)}\
        \nPercentage: {num_empty_test*100/len(test_labels)}"
    print(train_report_str)
    print(test_report_str)
    # Save into a txt file
    os.makedirs(f'results', exist_ok=True)
    saved_txt_path = 'empty_lbls.txt'
    if save_results:
        with open(os.path.join('results',saved_txt_path),'w') as f:
            f.write(train_report_str)
            f.write(test_report_str)
            f.close()
        
if __name__ == "__main__":
    dl = DataLoader()
    train, test = dl.get_train_path_list()
    num_empty = 0
    check_for_empty_label_files(train[1], test[1])
    show_bboxes(train, test)