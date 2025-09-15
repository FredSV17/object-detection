import os


class DataLoader:
    def __init__(self):
        self.base_path = "data"
        self.images_train_path = os.path.join(self.base_path, "train/images")
        self.labels_train_path = os.path.join(self.base_path, "train/labels")
        
        self.image_path_list = sorted([f"{self.images_train_path}/{img}" for img in os.listdir(self.images_train_path) if img.endswith('.jpg')])
        self.label_path_list = sorted([f"{self.labels_train_path}/{lbl}" for lbl in os.listdir(self.labels_train_path) if lbl.endswith('.txt')])
    
    def get_path_list(self):
        return self.image_path_list, self.label_path_list 
    