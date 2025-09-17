from data_loader import DataLoader
import os


def remove_empty_bounding_boxes(img_path_list, label_path_list):
    # Look for empty label files
    for img_path, lbl_path in zip(img_path_list, label_path_list):

        # Read the label file
        with open(lbl_path, 'r') as f:
            # read first character
            first_char = f.read(1)

            if not first_char:
                # Delete both image and label
                os.remove(img_path)
                os.remove(lbl_path)
                print(f"Removed: {img_path}")
        f.close()
        
if __name__ == "__main__":
    dl = DataLoader()
    img_path_list, label_path_list = dl.get_path_list()
    remove_empty_bounding_boxes(img_path_list, label_path_list)