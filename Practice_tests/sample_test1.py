'''Load a CSV file from the disk. Malformed rows should be skipped.
Filter submissions using an block-list of IP addresses.
Guess the country of a submission using a provided IP-lookup and appropriate fallback options. '''

import pandas as pd
file_location = '/Users/rmn7591/Documents/Repositories/hacking/coder/Practice_tests/logfile.xlsx'
df = pd.read_excel(file_location)
print(df)
f= open("logfile.xlsx",'r')
for line in f:
    print(line.split(''))