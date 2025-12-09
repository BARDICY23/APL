import pandas as pd

df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie'], 'Salary': [50000, 60000, 70000]})
df.to_excel('employees.xlsx', index=False)

df_read = pd.read_excel('employees.xlsx')
print(df_read[['Name', 'Salary']])
