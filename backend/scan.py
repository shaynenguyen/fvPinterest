from PIL import Image
import os


# Declaration
path = '../data'
firstAttempt = True
listWidth, listhHeight = ([] for i in range(2))

listImages = os.listdir(path)
print("Directory: ", len(listImages))

for img in listImages:
    with Image.open(path + '/' + img) as i:
        tempDetail = i.size
        listWidth.append(tempDetail[0])
        listhHeight.append(tempDetail[1])
        print(tempDetail)

print(listWidth)
print(listhHeight)