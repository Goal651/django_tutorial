import pandas as pd
import numpy as np

# Sample data
data = {
    'city': ['NYC', 'LA', 'NYC', 'Chicago', 'LA', 'Chicago', 'NYC', 'LA'],
    'price': [100, 200, 150, 300, 180, 250, 120, 210],
    'sold': [1, 0, 1, 0, 1, 0, 1, 1]  # Target: 1=sold, 0=not sold
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

unique_city = df['city'].unique()
print("\nUnique Countries:")
print(unique_city)
label_mapping = {city: i for i, city in enumerate(unique_city)}
print("\nLabel Mapping:")
print(label_mapping)
df['city_encoded_data']=df['city'].map(label_mapping)
print("\nData with encoded city:")
print(df)

