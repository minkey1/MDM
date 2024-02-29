def transpose(arr):
    return list(map(list, zip(*arr)))


def column(text,x=10,y=10,height=15.8,font_size=10):
    column = []
    for i in range(len(text)):
        column.append([text[i],x,y-i*height,font_size]) #Here the string needs to be replaced with text variable
    return column

def table(text,x=100,y=100,height=15.8,width=20,font_size=10):
    columns = transpose(text)
    table = []
    for i in range(len(columns)):
        clmn = column(columns[i],x+i*width,y,height,font_size)
        for j in range(len(clmn)):
            clmn[j][0]=str(clmn[j][0])
            table.append(clmn[j])
    return table
