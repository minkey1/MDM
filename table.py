#table.py
import utilities as pdf
import datetime as dt
import calendar as cl
import PDFPrep as pp
#pdf.DEBUG_MODE = True

def dates_in_month(year, month):
    # Get the number of days in the month
    num_days = cl.monthrange(year, month)[1]

    # Create a list of dates from 1 to the number of days in the month
    dates_list = [f"{day:02d}-{month:02d}-{year}" for day in range(1, num_days + 1)]    
    return dates_list


date = dt.datetime.today()
dateList = dates_in_month(date.year,date.month)

date_addable = pp.column(dateList, 101, 553.8, 15.8, 10)
pdf.add_text(date_addable,pdf_path="Cleaned-MDM-Blank-UC.pdf")

pdf.add_block([[60,546.7,36.7,15.7]])

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
table = pp.table(arr)
print(table)
#pdf.add_text(table)
pdf.add_text([["1.",73.4,548.7,10]],color='white')