import pandas as pd

file_path = r"D:\Shubham\Data Analytics Project\data\Aarogyasri_Jan2015_Report.csv"
file_delimiter = "@#$"
output_file_location = r"D:\Shubham\Data Analytics Project\data"
excel_file_path = output_file_location + "\\output.xlsx"

try:
    # Read CSV file into DataFrame
    df = pd.read_csv(file_path, sep=file_delimiter, engine='python', encoding='latin1')
    print("CSV file has been successfully read.")

    # Export DataFrame to Excel
    df.to_csv(excel_file_path, index=False)
    print('Data exported to Excel successfully!')
except Exception as e:
    print("Error occurred:", e)
