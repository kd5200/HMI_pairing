import pandas as pd
import openpyxl
import warnings
from openpyxl import workbook



wb = openpyxl.load_workbook(filename='/Applications/Python 3.11/Pop_data.xlsx')

active = wb.active



print(active)


# Read Excel file
# df = pd.read_csv('/Users/kd/Downloads/Pop_data.csv')

# sf = df['Sheet1']


# Display first few rows
# print(sf)