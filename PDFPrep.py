def transpose(arr):
    return list(map(list, zip(*arr)))


def column(text,x=100,y=100,separation=15.8,font_size=10):
    column = []
    for i in range(len(text)):
        column.append([text[i],x,y-i*separation,font_size]) #Here the string needs to be replaced with text variable
    return column

def row(text,x=100,y=100,separation=10,font_size=10):
    row = []
    for i in range(len(text)):
        row.append([text[i],x+i*separation,y,font_size]) #Here the string needs to be replaced with text variable
    return row

def table(text,x=100,y=100,separation_x=20,separation_y=15.8,font_size=10):
    #columns = transpose(text)
    columns = text
    table = []
    for i in range(len(columns)):
        clmn = column(columns[i],x+i*separation_x,y,separation_y,font_size)
        for j in range(len(clmn)):
            clmn[j][0]=str(clmn[j][0])
            table.append(clmn[j])
    return table

def column_block(number_of_blocks=3,x=100,y=100,w=100,h=100,separation=15.8):
    column = []
    for i in range(number_of_blocks):
        column.append([x,y-i*separation,w,h])
    return column