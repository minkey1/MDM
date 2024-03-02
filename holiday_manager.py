import utilities as pdf
import datetime as dt
import calendar as cl
import PDFPrep as pp

def dates_in_month(year, month):
    num_days = cl.monthrange(year, month)[1]
    return [f"{day:02d}-{month:02d}-{year}" for day in range(1, num_days + 1)]

def add_dates_column(year, month):
    date_list = dates_in_month(year, month)
    date_column = pp.column(date_list, 101, 553.8, 15.8, 9)
    pdf.add_text(date_column)

def row_numbers(num_days):
    return [f"{i+1}." for i in range(num_days)]

def alt_color_empty(empty,num_days):
    i=0
    while 2*i+1 < num_days:
        empty[2*i] = empty[2*i]+['#ebebeb']
        empty[2*i+1] = empty[2*i+1]+['white']
        i+=1

def holiday_table_template(num_days=31):
    boxes = pp.column_block(num_days, 60, 546.9, 36.7, 15.7, 15.8)
    number = pp.column(row_numbers(num_days), 78.2, 553.8, 15.8, 9)
    empty = pp.column_block(num_days, 154, 547.8, 397, 14, 15.8)
    alt_color_empty(empty, num_days)
    reason = pp.column(row_numbers(num_days), 347, 551.5, 15.8, 9)
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
    holidays.sort()
    holidays = pp.transpose(holidays)
    print_data = generate_print_data(holidays, holiday_table_template())
    render_holidays(print_data)

pdf.add_text(pdf_path='Cleaned-MDM-Blank-UC.pdf')
add_dates_column(2024, 6)
holidays = [[4, 'MILK'], [5, 'SUGAR'], [6, 'WHEAT'], [7, 'NICE'], [9, 'RICE']]
manage_holidays(holidays)
