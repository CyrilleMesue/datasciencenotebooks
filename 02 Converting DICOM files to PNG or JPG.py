#Author: Cyrille NJUME     
#Version: 02.07.2021

### Packages to be insalled
# pip install pydicom
# pip install pylibjpeg pylibjpeg-libjpeg pydicom
# pip install --upgrade numpy


### Import Packages
import numpy as np
import pydicom
import pylibjpeg
import os
import cv2
import dask
from tqdm.notebook import tqdm
from dask.diagnostics import ProgressBar
from pathlib import Path
```
### Code  

def Dicom_to_Image(input):
    """
    input: full dicom image path
    output: single channel image array with pixel values between 0 and 255
    """
    
    dcm_Img = pydicom.read_file(Path)

    rows = dcm_Img.get(0x00280010).value     #Get number of rows from tag (0028, 0010)
    cols = dcm_Img.get(0x00280011).value     #Get number of cols from tag (0028, 0011)

    #Instance_Number = int(dcm_Img.get(0x00200013).value)      #Get actual slice instance number from tag (0020, 0013)

    #Window_Center = dcm_Img.get(0x00281050).value    #Get window center from tag (0028, 1050)
    #Window_Width = dcm_Img.get(0x00281051).value     #Get window width from tag (0028, 1051)
    Window_Center = np.array(dcm_Img.WindowCenter)
    Window_Width = np.array(dcm_Img.WindowWidth)
    
    if Window_Center.size > 1:
      Window_Max = Window_Center[0] + Window_Width[0] / 2
      Window_Min = Window_Center[0] - Window_Width[0] / 2
    else:
      Window_Max = Window_Center + Window_Width / 2
      Window_Min = Window_Center - Window_Width / 2


    if (dcm_Img.get(0x00281052) is None):
        Rescale_Intercept = 0
    else:
        Rescale_Intercept = int(dcm_Img.get(0x00281052).value)

    if (dcm_Img.get(0x00281053) is None):
        Rescale_Slope = 1
    else:
        Rescale_Slope = int(dcm_Img.get(0x00281053).value)
    New_Img = np.zeros((rows, cols), np.uint8)
    Pixels = dcm_Img.pixel_array

    for i in range(0, rows):
        for j in range(0, cols):
            Pix_Val = Pixels[i][j]
            Rescale_Pix_Val = Pix_Val * Rescale_Slope + Rescale_Intercept

            if (Rescale_Pix_Val > Window_Max):       #if intensity is greater than max window
                New_Img[i][j] = 255
            elif (Rescale_Pix_Val < Window_Min):     #if intensity is less than min window
                New_Img[i][j] = 0
            else:
               New_Img[i][j] = int(((Rescale_Pix_Val - Window_Min) / (Window_Max - Window_Min)) * 255)     #Normalize the intensities
    output = New_Img
    
    return output


def dcm_to_png(filepath, outdir):
    """
        filepath: full dicom image path
        outdir: directory name where you want your image to be saved
    """
  image = Dicom_to_Image(filepath)
  dcm_filename = filepath.parts[-1]
  png_filename = dcm_filename.replace('.dcm','.png') # replace '.png' with '.jpg' to save image in jpeg format
  cv2.imwrite(outdir + png_filename, image) # image saved in outdir with png_filename in PNG format
  
  
outdir = '/Output Directory/' # Set directory where all png images will be saved
if not os.path.exists(outdir): # Loop to convert many images from dicom to PNG or JPEG
  os.mkdir(outdir)
  
dicom_img_paths = Path("/Input Directory/")  # Directory full of many dicom images to be converted
for imagepath in tqdm(dicom_img_paths):
  dcm_to_png(imagepath, outdir)
```


