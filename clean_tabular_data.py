import pandas as pd

data_df = pd.read_csv("MetaMarketplaceMLEng/Assets/Products.csv", lineterminator="\n")

print(data_df.isnull().sum())
print(f'URL duplicates: {data_df.duplicated(("url"), False).sum()}')