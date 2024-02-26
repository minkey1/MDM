import utilities as pdf


school_data = [
    ["Febuary 2024", 53, 751, 9],
    # Add more overlays as needed
]
pdf.add_text("Cleaned-MDM-Blank-UC.pdf", school_data, page_number=1)
#this function will add the text to the MDM pdf and give an output.pdf


table = [
    ["This is the table overlay", 200, 500, 12],
    # Add more overlays as needed
]
pdf.add_text("output.pdf", table, page_number=1)
#this will add more data to the output.pdf created by the function above


page2 = [
    ["This is the page 2 overlay", 200, 500, 12],
    # Add more overlays as needed
]
pdf.add_text("output.pdf", page2, page_number=2)
