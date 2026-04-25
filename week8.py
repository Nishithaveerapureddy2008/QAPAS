# file_handler.py

import pandas as pd

data = {"ID": ["1", "2"], "Score": [80, 90]}
df = pd.DataFrame(data)

df.to_csv("results.csv", index=False)

# read
df2 = pd.read_csv("results.csv")
print(df2)