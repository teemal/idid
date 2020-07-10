#!/home/teemal/anaconda3/bin/python
import sys
import os
import pygsheets
from datetime import date
from datetime import datetime
import pandas

#get cmnd line arg
value = sys.argv[1]
#get date/time
today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#auth 
cwd = os.getcwd()
gs = pygsheets.authorize(client_secret=cwd + 'client_secret.json')
#df with date time and cmnd line arg
df = pandas.DataFrame([[today, current_time, value]])
worksheet = gs.open('idid')
#check if 1st of month, if so make/use new sheet with month/year as title
month_year = str(date.today().month) + '/' + str(date.today().year)
if(date.today().day == 1):
    try:
        worksheet.add_worksheet(month_year,rows=6000, cols=10)
    except:
        #TODO
        #pygsheets doesnt have anything to detect existing sheet
        #hot garbage work around need to fix
        print('I keep trying to create a new sheet :(') 
#get last current sheet num
last_book = len(worksheet.worksheets()) - 1
#get last workbook
workbook = worksheet[last_book]
#last row for writing to
row = (str(len(workbook.get_col(1,  include_tailing_empty=False)) + 1))
write_row = 'A' + row
#write to cell
workbook.set_dataframe(df, write_row, copy_head=False)
