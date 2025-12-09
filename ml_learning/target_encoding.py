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
mean_target=df.groupby('city')['sold'].mean()
print("\nMean Target:")
print(mean_target)
df['city_encoded_data']=df['city'].map(mean_target)
print("\nData with encoded city:")
print(df)
