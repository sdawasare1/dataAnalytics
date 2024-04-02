import pandas as pd

file_path = r"D:\Shubham\Data Analytics Project\data\output.csv"

try:
    # Read the first line of the Excel file into a DataFrame
    df = pd.read_excel(file_path, nrows=1)
    print("First line of the Excel file has been successfully read:")
    print(df)

except Exception as e:
    print("Error occurred:", e)