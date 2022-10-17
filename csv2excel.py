#csv2excel.py
#Created by JGallo 2022/7/12
#Converts .csv to .xlsx
import pandas as pd
import argparse, openpyxl

parser = argparse.ArgumentParser(description='Converts .csv files to .xlsx format')
parser.add_argument('-i', '--input')
args = parser.parse_args()

if(args.input == None):
    parser.print_help(file=None)
else:
    try:
        data = pd.read_csv(str(args.input))
        output = str(args.input).replace('.csv','') + '.xlsx'
        data.to_excel(output, index=False)
        print('File=' + str(args.input) + ' converted to .xlsx format')
    except FileNotFoundError:
        print('No such file or directory: ' + str(args.input))
    
