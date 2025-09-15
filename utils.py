import matplotlib.pyplot as plt
import os

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