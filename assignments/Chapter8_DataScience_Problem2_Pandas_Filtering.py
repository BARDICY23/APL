import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 28], 'Score': [85, 75, 92]})
print(df[df['Score'] > 80])
