from PIL import Image
import pandas as pd
import os

# Database Stuff
from database import engine, session
from models import Images

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

# Create Dataframe
df = pd.DataFrame(zip(listImages, listWidth, listhHeight), columns=['name','width','height'])
print(df)

df.to_sql(name='images', con=engine, if_exists='replace', index=True)