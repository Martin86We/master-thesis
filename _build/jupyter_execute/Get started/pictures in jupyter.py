# Arbeiten mit Bildern in Jupyter Notebook

## Bibliotheken:

import os
os.getcwd() # get working directory
#change working directory
os.chdir('C://Users//Martin//Desktop//jupyter_Book_data//2020-jupyterbook-with-turing-way-master')
os.getcwd() # get working directory

import numpy as np
from PIL import Image

img = Image.open("my_jupyter-book/figures/philips 28x28_gray.jpg") # hier rgb bild einlesen um Farbkanal zu haben
np_img = np.array(img)
np_img.shape

Wie setzt sich ein Bild in einem Array zusammen?
Hier den Aufbau eines Bildes veranschaulichen:

## Bei Quadratischen Bildern:

### Einlesen als Graustufenbild:

### Shape:

### Resize:

### In Graustufen umwandeln:

### IMG to Numpy Array:

### Speichern:

## Mehrere Bilder in ein Array laden: