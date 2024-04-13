import utilities as pdf
import datetime as datetime
import calendar as calendar
import PDFPrep as prep
import numpy as np

HOLIDAYS_INPUT = [[4, 'Please'], [5, 'Enter'], [6, 'Holidays'],[7,'Details'], [8, 'Before'], [9, 'Launching']]
MONTH = 10
YEAR = 2004

def get_dates_in_month(year, month):
    num_days = calendar.monthrange(year, month)[1]
    return [f"{day:02d}-{month:02d}-{year}" for day in range(1, num_days + 1)]

def find_sundays(year, month): #finds the dates of sundays in the month
    sundays = []
    cal = calendar.Calendar()
    for day in cal.itermonthdays(year, month):
        if day != 0:  
            weekday = calendar.weekday(year, month, day)
            if weekday == 6:  
                sundays.append(day)
    return sundays

def get_sundays_data(year=2004, month=10): #converts sundays to holiday format with - - S U N D A Y - - as reason
    sunday_dates = find_sundays(year, month)
    sunday_holidays = [sunday_dates,[]]
    for i in sunday_dates:
        sunday_holidays[1]+=['- - S U N D A Y - -']
    return sunday_holidays

def add_dates_column(year, month): 
    date_list = get_dates_in_month(year, month)
    date_column = prep.column(date_list, 101, 553.8, 15.8, 9)
    pdf.add_text(date_column)

def get_row_numbers(num_days):
    return [f"{i+1}." for i in range(num_days)]

def alternate_color_empty(empty,num_days):
    i=1
    while 2*i <= num_days:
        empty[2*i] = empty[2*i]+['#ebebeb']
        empty[2*i-1] = empty[2*i-1]+['white']
        i+=1

def prepare_holiday_table_template(num_days=31):
    boxes = prep.column_block(num_days, 60, 546.9, 36.7, 15.7, 15.8)
    number = prep.column(get_row_numbers(num_days), 78.2, 553.8, 15.8, 9)
    empty = prep.column_block(num_days, 154, 547.2, 397, 15, 15.8)
    alternate_color_empty(empty, num_days)
    reason = prep.column(get_row_numbers(num_days), 347, 551.5, 15.8, 9)
    return number, boxes, empty, reason

def render_holidays(print_data):
    pdf.add_block(print_data[1])
    pdf.add_text(print_data[0], color='white', alignment='center')
    pdf.add_block(print_data[2])
    pdf.add_text(print_data[3], alignment='center')

def generate_print_data(holidays, days):
    print_data = [[], [], [], []]
    for i in holidays[0]:
        for j in range(len(days)):
            print_data[j].append(days[j][i-1])
    for i in range(len(holidays[0])):
        print_data[3][i][0] = holidays[1][i]
    return print_data

def manage_holidays(holidays):
    print_data = generate_print_data(holidays, prepare_holiday_table_template())
    render_holidays(print_data)

def food_table_data(input_list,table_number=1):
    data = [
    input_list,                                       # Original list
    [round(i *((50+(table_number)*50)/1000), 2) if isinstance(i, (int, float)) else '' for i in input_list],  # Divided by 10, None if not a number
    [round(i *((50+(table_number)*50)/1000), 2) if isinstance(i, (int, float)) else '' for i in input_list],  # Repeated, can change or remove
    [i *(15+((table_number-1)*5)) if isinstance(i, (int, float)) else '' for i in input_list]   # Multiplied by 15, None if not a number
]
    return data

def render_food_table(data,table_number=1):
    table = prep.table(data, (table_number-1)*193+180, 550, (table_number-1)*4+47)
    pdf.add_text(table, alignment='center')


if __name__ == '__main__':
    pdf.add_text(pdf_path='Cleaned-MDM-Blank-UC.pdf')
    add_dates_column(YEAR, MONTH)
    manage_holidays(get_sundays_data(YEAR, MONTH))
    holidays = HOLIDAYS_INPUT
    holidays.sort()
    holidays = prep.transpose(holidays)
    manage_holidays(holidays)
    table1 = food_table_data((51,52,'','','','','','','','',511,512,513,514,515,516,'',518,519,520,521,522,523,'',525,526,527,528,529,530,''),1)
    table2 = food_table_data((51,52,'','','','','','','','',511,512,513,514,515,516,'',518,519,520,521,522,523,'',525,526,527,528,529,530,''),2)
    render_food_table(table1,1)
    render_food_table(table2,2)