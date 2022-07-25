## Facebook Marketplace Search Ranking
Facebook marketplace uses a Search Ranking system to help users better find what they are looking for. This is based on complex unstrucutred data like images and text. The marketplace leverages computer vision and natural language processing (NLP) techniques to deliver the service. For more information [see here](https://engineering.fb.com/2018/10/02/ml-applications/under-the-hood-facebook-marketplace-powered-by-artificial-intelligence/).

## Source Data
There were three sources of data which were then cleansed, transformed, and combined. This data was sourced from gumtree to get product images and their relevant product descriptions among other features. The below explains the data source:

• Products.csv - Tabular dataset holding data relevant to the product such as the uid, description, price and location. This data includes the label (category) that will be the target variable for the mulit-class classification prediction.
• Images.csv - Tabular dataset holding data relevant to the images, including the uid for the product the image relates to.
NOTE: Multiple images exist for some products
• image_folder - This holds the actual image file in jpg format.
NOTE: Not included here due to size

## Data Preparation
In order to prepare the data for training purposes it was required to both cleanse Tabular data and merge. 
<-! In addition, a holdout sample of the images was created for downstream testing of the API. ->

The following programs were created to prodvide the nescessary fucntionality for cleansing the data:

clean_tabular.py - This program creates a class (TabularCleanse) which includes various methods for common functions for data cleansing
clean_images.py - This program creates a class (ImageCleanse) which includes various methods for common functions for image cleansing.
The above were then used in the following programs to perform the data cleanse:

cleanse_tabular.py - used to transform the products.csv data into the pickle file 'clean_cat_data.pkl'. The key functions applied are
Removing null values and outliers from price
Converting price from string to float
Splitting columns to increase features
Dropping colunms not required for further development
cleaned_images.py - used to transform the images and create a holdout sample of images. Creates pickle file 'cleansed_img_tabular' to hold data for those images not in the holdout sample. The following transformations are applied:
Images are resized to 64x64 using the same ratio as input with black padding applied.
cleanse_product_images.py - used to merge and transform pickle files 'products_cleansed.pkl' & 'cleansed_img_tabular' to create one file 'cleansed_product_images.pkl'. Products without images are dropped.
NOTE: 'cleansed_product_images.npy' also output in order to build and train model using google colab for gpu access.

## Linear Regression Model

## Data classification
• simp_classification.py - Trains a simple binary model using the image numpy and category. 
Model has an accuracy of 0.09.
Improvements: Increase image size. 

<-! Lessons Learnt 
Downloading programms on ubuntu:
sudo sudo apt install python3-opencv-python

-> 
