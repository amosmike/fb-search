import pandas as pd
from PIL import Image
import os, os.path

base_dir = '/home/ubuntu/images'
clean_dir = '/home/ubuntu/clean_images'

isExist = os.path.exists(clean_dir)

if isExist == True:
    pass
else:
    os.mkdir(r'clean_images')

os.chdir(clean_dir)

clean_image_data = {'id': [], 'width': [], 'height': [], 'mode': []}

for root,dirs,files in os.walk(base_dir):
    for file in files:
        try: 
            path = os.path.join(base_dir, file)
            img = Image.open(path)
            new_img = img.resize((790, 860))
            new_img = new_img.convert('RGB')
            
            new_img.save(f'{str(file)}')

            mode = new_img.mode
            width = new_img.width
            height = new_img.height
            id = str(file)

                      
            clean_image_data['id'].append(id)
            clean_image_data['width'].append(width)
            clean_image_data['height'].append(height)
            clean_image_data['mode'].append(mode)
        
        except:
            print("error")
            pass

# Takes 8 mins to run
        
# Make df
clean_image_data = pd.DataFrame(clean_image_data)

# Checks
print(clean_image_data["width"].unique())
print(clean_image_data["height"].unique())
print(clean_image_data["mode"].unique())