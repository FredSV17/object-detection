import kagglehub
import os



if __name__ == '__main__':
    kaggle_path = "thepbordin/indoor-object-detection"
    # Download latest version
    path = kagglehub.dataset_download(kaggle_path)

    print("Path to dataset files:", path)