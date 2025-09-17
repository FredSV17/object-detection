import matplotlib.pyplot as plt
import os
import cv2

def plot_area_distribution(area_list):
    # Plot the distribution of areas
    plt.hist(area_list, bins=10)
    plt.xlabel('Area')
    plt.ylabel('Frequency')
    plt.title('Distribution of Bounding Box Areas')
    os.makedirs(f'results/analysis', exist_ok=True)
    plt.savefig('results/analysis/area_bbox_graph.png')
    
def get_area(points):
    # Get the area of the bounding box
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)
    return (x_max - x_min) * (y_max - y_min)

#TODO: create bounding box heatmap
#def create_heatmap(bb_list):
def show_image_bbox(img, bbox_list):
    new_img = img
    h_img, w_img, _ = img.shape
    for polygon in bbox_list:
        value_list = list(map(float, polygon.split()[1:]))
        x_c, y_c, h, w = value_list
        x_min = int((x_c - w/2) * w_img)
        x_max = int((x_c + w/2) * w_img)
        y_min = int((y_c - h/2) * h_img)
        y_max = int((y_c + h/2) * h_img)
        cv2.rectangle(new_img, (x_min,y_min), (x_max, y_max), (0, 255, 0), 2)
    return new_img

def show_bboxes(train, test):
    zipped_train = zip(train[0], train[1])
    for img_path, lbl_path in zip(train[0], train[1]):
        # Read the image
        image = cv2.imread(img_path)
        
        # Read the label file
        with open(lbl_path, 'r') as f:
            bbox_list = f.readlines()
        img_name, extension = os.path.splitext(os.path.basename(img_path))
        new_img = show_image_bbox(image, bbox_list)
        # Create directory 
        os.makedirs(f'bounding_boxes/train', exist_ok=True)
                
        cv2.imwrite(f'bounding_boxes/train/{img_name + extension}', new_img)
    for img_path, lbl_path in zip(test[0], test[1]):
        # Read the image
        image = cv2.imread(img_path)
        
        # Read the label file
        with open(lbl_path, 'r') as f:
            bbox_list = f.readlines()
        img_name, extension = os.path.splitext(os.path.basename(img_path))
        new_img = show_image_bbox(image, bbox_list)
        # Create directory 
        os.makedirs(f'bounding_boxes/test', exist_ok=True)
                
        cv2.imwrite(f'bounding_boxes/test/{img_name + extension}', new_img)
