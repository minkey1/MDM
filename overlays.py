import utilities as pdf


school_data = [
    ["Febuary 2024", 53, 751, 9],
    ["School name",135,690,12],
    ["Bank name",140,660,12],
    ["Gram Panchayat",310,690,12],
    ["Khata Syankha",265,660,12],
    ["IFSC code",405,660,12],
    ["Block",440,690,12],
    ["1 to 5",285,640,11],
    ["6 to 8",405,640,12],
    ["mobile1",210,622,12],
    ["mobile2",415,622,12],
    # Add more overlays as needed
]
pdf.add_text("Cleaned-MDM-Blank-UC.pdf", school_data, page_number=1)
#this function will add the text to the MDM pdf and give an output.pdf


table = [
    ["s68",350,550, 12],
    ["date",100,550,12],
    ["s15",157,550,12],
    ["w15",210,550,12],
    ["r15",260,550,12],
    ["m15",305,550,12],
    ["w68",405,550,12],
    ["r68",459,550,12],
    ["m68",507,550,12],
    ["date2",100,534,12], #16 difference per row
    # Add more overlays as needed
]
pdf.add_text("output.pdf", table, page_number=1)
#this will add more data to the output.pdf created by the function above


page2 = [
    ["15w3", 134,580, 12],
    ["15r3",134,566, 12],
    ["68w3",134,552,12],
    ["68r3",134,538,12],
    ["4",167,580,12],
    ["5",167,565,12],
    ["6",167,552,12],
    ["7",167,538,12],
    ["t1",134,525,12],
    ["t2",167,525,12],
    ["p1",134,513,12],
    ["p2",167,513,12],

    ["5*",208,580,12],
    ["6*",248,580,12],
    ["7*",283,580,12],
    ["8*",343,580,12],
    ["9*",393,580,12],
    ["10*",440,580,12],
    ["11*",475,580,12],
    ["12*",515,580,12],
    # Add more overlays as needed
]
pdf.add_text("output.pdf", page2, page_number=2)

page2 = [
    
    # Add more overlays as needed
]
pdf.add_text("output.pdf", page2, page_number=2)
