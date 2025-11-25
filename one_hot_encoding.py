import pandas as pd

data = {"color": ["yellow", "red", "green"], "size": ["L", "M", "S"]}

df = pd.DataFrame(data)

one_hot_encoded_df = pd.get_dummies(df, columns=["color","size"])
one_hot_encoded_df = one_hot_encoded_df.astype(int)

print(one_hot_encoded_df.T)
