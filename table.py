#table.py
import utilities as pdf
import datetime as dt
import calendar as cl
import PDFPrep as pp
#pdf.DEBUG_MODE = True



def dates_in_month(year, month): #returns the 01/02/2024.... text list
    # Get the number of days in the month
    num_days = cl.monthrange(year, month)[1]

    # Create a list of dates from 1 to the number of days in the month
    date_list = [f"{day:02d}-{month:02d}-{year}" for day in range(1, num_days + 1)]    
    return date_list


def add_dates_column(year,month): #renders the dates on pdf
    date_list = dates_in_month(year, month)
    date_column = pp.column(date_list, 101, 553.8, 15.8, 9)
    pdf.add_text(date_column)


def row_number(num_days):
    text_list = []
    for i in range(num_days):
        text_list.append(f"{i+1}.")
    return text_list

def alt_color_empty(empty,num_days):
    i=0
    while 2*i+1 < num_days:
        empty[2*i] = empty[2*i]+['#ebebeb']
        empty[2*i+1] = empty[2*i+1]+['white']
        i+=1

def holiday_table_template(num_days=31): #returns template for column data for text and blocks, blacks are transparent by default
    boxes = pp.column_block(num_days,60,546.9,36.7,15.7,15.8)   
    number = pp.column(row_number(num_days),78.2, 553.8, 15.8, 9)
    empty = pp.column_block(num_days,154,547.8,397,14,15.8)
    alt_color_empty(empty,num_days)

    reason = pp.column(row_number(num_days),347, 551.5, 15.8, 9)
    return (number,boxes,empty,reason)

def render_holidays(print_data):
    pdf.add_block(print_data[1])
    pdf.add_text(print_data[0], color='white', alignment='center')
    pdf.add_block(print_data[2])
    pdf.add_text(print_data[3], alignment='center')

def generate_print_data(holidays, days):
    # Generate print data based on holidays and days
    print_data = [[], [], [], []]  # Since there are only four sublists number, block, empty, reason

    for i in holidays[0]:
        for j in range(len(days)):
            print_data[j].append(days[j][i-1])

    for i in range(len(holidays[0])):
        print_data[3][i][0] = holidays[1][i]

    return print_data


def manage_holidays(holidays):
    
    holidays.sort()   # Sort holidays    
    holidays = pp.transpose(holidays)  # Transpose holidays
    print_data = generate_print_data(holidays, holiday_table_template())  # Generate holiday data from holiday template
    render_holidays(print_data)  # Render holidays



pdf.add_text(pdf_path='Cleaned-MDM-Blank-UC.pdf')
add_dates_column(2024,6)
holidays = [[2,'MILK'],[5,'SUGAR'],[8,'WHEAT'],[23,'NICE'],[9,'RICE']]
manage_holidays(holidays)