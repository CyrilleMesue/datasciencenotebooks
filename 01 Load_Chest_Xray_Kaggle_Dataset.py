# Author : Cyrille Mesue NJUME
# Version 01-07-2021
resize_shape = (224,224)

def load_Xray_train_data(splittype, resize_shape):
    import numpy as np
    from PIL import Image
    
    X = []
    y = []
    
    if splittype == "train": # Loads the training dataset
        
        train_normal_images = "./chest_xray/train/NORMAL/" # Directory where the normal examples for the training dataset are located
        train_pneumonia_images = "./chest_xray/train/PNEUMONIA/" # Directory where the disease examples for the training dataset are located
        X_train = []
        y_train = []

        normal_img_paths = sorted([os.path.join(train_normal_images, fname) for fname in os.listdir(train_normal_images)
                                   if fname.endswith(".jpeg") and not fname.startswith(".")])

        pneumonia_img_paths = sorted([os.path.join(train_pneumonia_images, fname) for fname in os.listdir(train_pneumonia_images)
                                      if fname.endswith(".jpeg") and not fname.startswith(".")])

        m = len(pneumonia_img_paths)
     
        for ii in range(m):
            image = np.array(Image.open(pneumonia_img_paths[ii]).convert('L').resize(resize_shape))
            X_train.append(image)
            y_train.append(1)
            
        n = len(normal_img_paths)
        for jj in range(n):
            image = np.array(Image.open(normal_img_paths[jj]).convert('L').resize((resize_shape)))
            X_train.append(image)
            y_train.append(0)
            
        X = X_train
        y = y_train
            
    elif splittype == "dev": # Loading the validation set
        
        dev_normal_images = "./chest_xray/dev/NORMAL/" # Directory where the normal examples for the validation dataset are located
        dev_pneumonia_images = "./chest_xray/dev/PNEUMONIA/" # Directory where the diseased examples for the validation dataset are located
        
        normal_img_paths = sorted([os.path.join(dev_normal_images, fname) for fname in os.listdir(dev_normal_images)
                                   if fname.endswith(".jpeg") and not fname.startswith(".")])

        pneumonia_img_paths = sorted([os.path.join(dev_pneumonia_images, fname) for fname in os.listdir(dev_pneumonia_images)
                                      if fname.endswith(".jpeg") and not fname.startswith(".")])
        X_dev = []
        y_dev = []

        #m = len(pneumonia_img_paths)
        m = 100
        for ii in range(12):
            image = np.array(Image.open(pneumonia_img_paths[ii]).convert('L').resize(resize_shape))
            X_dev.append(image)
            y_dev.append(1)

        #n = len(normal_img_paths)
        n = 100
        for jj in range(n):
            image = np.array(Image.open(normal_img_paths[jj]).convert('L').resize(resize_shape))
            X_dev.append(image)
            y_dev.append(0)
            
        X = X_dev
        y = y_dev
            
    elif splittype == "test": # Loading the test set
        
        test_normal_images = "./chest_xray/test/NORMAL/" # Directory where the normal examples for the test dataset are located
        test_pneumonia_images = "./chest_xray/test/PNEUMONIA/"  # Directory where the diseased examples for the test dataset are located

        normal_img_paths = sorted([os.path.join(test_normal_images, fname) for fname in os.listdir(test_normal_images)
                                   if fname.endswith(".jpeg") and not fname.startswith(".")])

        pneumonia_img_paths = sorted([os.path.join(test_pneumonia_images, fname) for fname in os.listdir(test_pneumonia_images)
                                      if fname.endswith(".jpeg") and not fname.startswith(".")])
        X_test = []
        y_test = []

        #m = len(pneumonia_img_paths)
        m = 100

        for ii in range(m):
            image = np.array(Image.open(pneumonia_img_paths[ii]).convert('L').resize(resize_shape))
            X_test.append(image)
            y_test.append(1)

        #n = len(normal_img_paths)
        n = 100
        for jj in range(n):
            image = np.array(Image.open(normal_img_paths[jj]).convert('L').resize(resize_shape))
            X_test.append(image)
            y_test.append(0)
            
        X = X_test
        y = y_test
    
    X = np.array(X)
    y = np.array(y)

    return X, y
