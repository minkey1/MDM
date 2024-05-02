import utilities as pdf
import datetime as datetime
import calendar as calendar
import PDFPrep as prep
import time

#pdf.DEBUG_MODE = True
MONTH = 10
YEAR = 2004
HOLIDAYS_INPUT = [[4, 'Please'], [5, 'Enter'], [6, 'Holidays'],[7,'Details'], [8, 'Before'], [9, 'Launching']]
STUDENT_DATA1 = [1,2,'-','-','-','-','-','-','-','-',11,12,13,14,15,16,'-',18,19,20,21,22,23,'-',25,26,27,28,29,30,'-']
STUDENT_DATA2 = [51,52,'-','-','-','-','-','-','-','-',511,512,513,514,515,516,'-',518,519,520,521,522,523,'-',525,526,527,528,529,530,'-']
#STUDENT_DATA2 = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
WHEAT_DAYS = [1,11,13,15,19,21,23,25,27,29]


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
    date_column = prep.column(date_list, 124, 553.8, 15.8, 10)
    pdf.add_text(date_column, alignment='center')

def get_row_numbers(num_days):
    return [f"{i+1}." for i in range(num_days)]

def alternate_color_empty(empty,num_days):
    for i in range(num_days):
        if i%2 == 0:
            empty[i] = empty[i]+['#ebebeb']
        else:
            empty[i] = empty[i]+['white']

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
    [i *((50+table_number*50)) if isinstance(i, (int, float)) else '-' for i in input_list],  # Divided by 10, None if not a number
    [i *((50+table_number*50)) if isinstance(i, (int, float)) else '-' for i in input_list],  # Repeated, can change or remove
    [i *(15+(table_number-1)*5) if isinstance(i, (int, float)) else '-' for i in input_list]   # Multiplied by 15, None if not a number
]
    return data

def render_food_table(data,table_number=1):
    unit_converted_data = [[str(round(element / 1000,2)) + "K" if isinstance(element, (int, float)) and element > 1000 else element for element in row] for row in data]
    unit_converted_data[0] = data[0] # reverts the number of students so it doesn't get converted
    table = prep.table(unit_converted_data, (table_number-1)*193+180, 550, (table_number-1)*4+47)
    pdf.add_text(table, alignment='center')

def render_table_sum(sum_list, table_number=1):# Assuming sum_table is your 1D array
    unit_converted_data = [str(round(element / 1000, 2)) + "K" if isinstance(element, (int, float)) and element > 1000 else str(element) for element in sum_list]
    unit_converted_data[0] = str(sum_list[0]) # reverts the number of students so it doesn't get converted
    
    for i in range(0,len(unit_converted_data)):
        if unit_converted_data[i] in ['0','0K',0]:
            unit_converted_data[i] = '-'
    
    sum_row_data = prep.row(unit_converted_data, (table_number-1)*193+180, 62, (table_number-1)*4+47)
    pdf.add_text(sum_row_data, alignment='center')

def render_counter_row(counter_row, table_number=1):
    counter_row = [str(element) for element in counter_row]

    for i in range(0,len(counter_row)):
        if counter_row[i] in ['0','0K',0]:
            counter_row[i] = '-'
    
    counter_row_data = prep.row(counter_row, (table_number-1)*193+180, 48, (table_number-1)*4+47)
    pdf.add_text(counter_row_data, alignment='center')

def counter_row(data):
    counter_row = [0,0,0,0]
    for i in range(len(data)):
        count=0
        for x in data[i]: 
            if isinstance(x, (int, float)):
                count+=1
        counter_row[i] = count
    return counter_row

def remove_wheat(data, wheat_days):
        days = calendar.monthrange(YEAR, MONTH)[1]
        for i in range(1,days+1):
            if i in wheat_days:
                data[1][i-1] = '-'
            else:
                data[2][i-1] = '-'

def length_of_data_check(data):
    if len(data) != calendar.monthrange(YEAR, MONTH)[1]:
        while len(data) > calendar.monthrange(YEAR, MONTH)[1]:
            data.pop()
    return data

def table_manager():
    add_dates_column(YEAR, MONTH)
    table1 = food_table_data(length_of_data_check(STUDENT_DATA1),1)
    table2 = food_table_data(length_of_data_check(STUDENT_DATA2),2)
    remove_wheat(table1,WHEAT_DAYS)
    remove_wheat(table2,WHEAT_DAYS)
    sum1 = [sum(filter(lambda x: isinstance(x, (int,float)), sublist)) for sublist in table1]
    sum2 = [sum(filter(lambda x: isinstance(x, (int,float)), sublist)) for sublist in table2]
    TOTAL_STUDENTS1 = sum1[0]
    TOTAL_STUDENTS2 = sum2[0]
    render_food_table(table1,1)
    render_food_table(table2,2)
    render_table_sum(sum1,1)
    render_table_sum(sum2,2)
    counter1 = counter_row(table1)
    counter2 = counter_row(table2)
    render_counter_row(counter1,1)
    render_counter_row(counter2,2)
    manage_holidays(get_sundays_data(YEAR, MONTH))
    holidays = HOLIDAYS_INPUT
    holidays.sort()
    holidays = prep.transpose(holidays)
    manage_holidays(holidays)
    return TOTAL_STUDENTS1, TOTAL_STUDENTS2


if __name__ == '__main__':
    pdf.add_text(pdf_path='Cleaned-MDM-Blank-UC.pdf')
    table_manager()
