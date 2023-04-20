import pandas as pd


file = pd.read_excel("file.xlsx")  # get table one
file2 = pd.read_excel("file.xlsx", sheet_name="Address")  # get table two by name
file3 = pd.read_excel("file.xlsx", sheet_name=1)  # get table two by index
file4 = pd.read_excel("file.xlsx", sheet_name=0, usecols=[0])  # get table one by index and specific columns by index
file5 = pd.read_excel("file.xlsx", sheet_name=0, usecols="A:B")  # get table one by index and specific columns by name
file6 = pd.read_excel("file.xlsx", sheet_name=None)  # get all the data from the file (table one and table two)
file7 = pd.read_excel("file.xlsx", sheet_name=1, usecols="A:B", skiprows=3)  # get specific columns and skip columns from index 3
file8 = pd.read_excel("file.xlsx", sheet_name=0, usecols="A:B", nrows=2)  # get specific columns from index 2
file9 = pd.read_excel("file.xlsx", sheet_name=None)  # get all the data from the file (table one and table two)

print(file)


