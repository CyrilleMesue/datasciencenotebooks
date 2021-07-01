# Author : Cyrille Mesue NJUME
# Version 01-07-2021


def load_Xray_train_data(splittype):
    import numpy as np
    from PIL import Image
    
    X = []
    y = []
    
    if splittype == "train":
        
        train_normal_images = "./chest_xray/train/NORMAL/"
        train_pneumonia_images = "./chest_xray/train/PNEUMONIA/"
        X_train = []
        y_train = []

        normal_img_paths = sorted([os.path.join(train_normal_images, fname) for fname in os.listdir(train_normal_images)
                                   if fname.endswith(".jpeg") and not fname.startswith(".")])

        pneumonia_img_paths = sorted([os.path.join(train_pneumonia_images, fname) for fname in os.listdir(train_pneumonia_images)
                                      if fname.endswith(".jpeg") and not fname.startswith(".")])

        m = len(normal_img_paths)

        for ii in range(m):
            image = np.array(Image.open(pneumonia_img_paths[ii]).resize((200,200)))
            X_train.append(image)
            y_train.append(1)

        for ii in range(m):
            image = np.array(Image.open(normal_img_paths[ii]).resize((200,200)))
            X_train.append(image)
            y_train.append(0)
            
        X = X_train
        y = y_train
            
    elif splittype == "dev":
        
        dev_normal_images = "./chest_xray/dev/NORMAL/"
        dev_pneumonia_images = "./chest_xray/dev/PNEUMONIA/"
        
        normal_img_paths = sorted([os.path.join(dev_normal_images, fname) for fname in os.listdir(dev_normal_images)
                                   if fname.endswith(".jpeg") and not fname.startswith(".")])

        pneumonia_img_paths = sorted([os.path.join(dev_pneumonia_images, fname) for fname in os.listdir(dev_pneumonia_images)
                                      if fname.endswith(".jpeg") and not fname.startswith(".")])
        X_dev = []
        y_dev = []

        m = len(normal_img_paths)

        for ii in range(m):
            image = np.array(Image.open(pneumonia_img_paths[ii]).resize((200,200)))
            X_dev.append(image)
            y_dev.append(1)

        for ii in range(m):
            image = np.array(Image.open(normal_img_paths[ii]).resize((200,200)))
            X_dev.append(image)
            y_dev.append(0)
            
        X = X_dev
        y = y_dev
            
    elif splittype == "test":
        
        test_normal_images = "./chest_xray/test/NORMAL/"
        test_pneumonia_images = "./chest_xray/test/PNEUMONIA/"

        normal_img_paths = sorted([os.path.join(test_normal_images, fname) for fname in os.listdir(test_normal_images)
                                   if fname.endswith(".jpeg") and not fname.startswith(".")])

        pneumonia_img_paths = sorted([os.path.join(test_pneumonia_images, fname) for fname in os.listdir(test_pneumonia_images)
                                      if fname.endswith(".jpeg") and not fname.startswith(".")])
        X_test = []
        y_test = []

        m = len(normal_img_paths)

        for ii in range(m):
            image = np.array(Image.open(pneumonia_img_paths[ii]).resize((200,200)))
            X_test.append(image)
            y_test.append(1)

        for ii in range(m):
            image = np.array(Image.open(normal_img_paths[ii]).resize((200,200)))
            X_test.append(image)
            y_test.append(0)
            
        X = X_test
        y = y_test
    
    X = np.array(X)
    y = np.array(Y)

    return X, y
    


# In[ ]:




