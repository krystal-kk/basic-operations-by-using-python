import shutil, os
import pandas as pd

content = pd.read_csv("/home/jaran/Downloads/ISIC2016/train/trainGT.csv")   #read the csv file
content = content.sort_values('label')   #sort the content according to the column of label

# category = ['benign', 'malignant']     #if the category is small, use a list directly
category = list(content.label.unique())   #get a list of categories, 

all_images = '/home/jaran/Downloads/ISIC2016/orimage/Train/'
new_images = '/home/jaran/Downloads/ISIC2016/train/'

for i in category:
    os.makedirs(os.path.join(new_images, i))

#moving the image files to their respective categories
for i in category:
    for j in list(content[content['label']==i]['id']):   #image id
        get_image = os.path.join(all_images, j+'.jpg')
        move_image = shutil.move(get_image, new_images+i)