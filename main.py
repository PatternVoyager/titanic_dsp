mport pandas as pd
import sys
import os

def getfile_by_args():
    if len(sys.argv)>1:
        filename = sys.argv[1]
        if filename.lower().endswith('.csv'):
            return filename
        else:
            return None
    return None

def getfile_by_input():
    filename = getfile_by_args()
    if filename is None:
        while True:
            filename = input('enter your file name (example.csv): ').strip()
            if filename:
                if filename.lower().endswith('.csv'):
                    return filename
                else:
                    print('file must end with .csv. please try again')
            else:
                print('file name cannot be empty. please try again')
    return filename

def main():
    filename = getfile_by_input()
    if not os.path.exists(filename):
        print(f'Error: file \'{filename}\' not found')
        return
    read_file = pd.read_csv(filename)
    print(read_file.head())
