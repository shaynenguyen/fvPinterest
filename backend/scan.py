from PIL import Image
import pandas as pd
from config import SERVER_HOST, DATA_FOLDER
import os, re

# Database Stuff
from database import engine, session
from models import Images

# Declaration
ext = r"(\..[^\s]+)"

listWidth, listhHeight = ([] for i in range(2))

listImages = os.listdir(DATA_FOLDER)
print("Directory: ", len(listImages))

for img in listImages:
    with Image.open(DATA_FOLDER + '/' + img) as i:
        tempDetail = i.size
        listWidth.append(tempDetail[0])
        listhHeight.append(tempDetail[1])
        print(tempDetail)

listUrl = [SERVER_HOST +'uploads/'+ i for i in listImages]
listImages = [re.sub(ext,"", i) for i in listImages]

print(listWidth)
print(listhHeight)

# Create Dataframe
df = pd.DataFrame(zip(listImages, listUrl, listWidth, listhHeight), columns=['name','url','width','height'])
print(df)

df.to_sql(name='images', con=engine, if_exists='replace', index=True)
df.info()