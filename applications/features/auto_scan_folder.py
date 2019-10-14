import os
from PIL import Image

setPath = 'data/'

dataFolder = os.listdir(setPath)

dataInfo = [Image.open(setPath + img) for img in dataFolder]

print([img.size for img in dataInfo])

# print(Image.open(setPath + dataFolder[3]).size)