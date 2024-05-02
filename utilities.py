#utilities.py
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io

INPUT_FILE = "output.pdf"
SYSTEM_FILE = "output.pdf"
DEBUG_MODE = False

def open_pdf(pdf_path):
    """Open PDF file and return PdfReader object."""
    try:
        return PdfReader(open(pdf_path, "rb"))
    except Exception as e:
        print(f"An error occurred: {e}. Creating a new A4 PDF.")
        create_empty_pdf(SYSTEM_FILE, page_size=A4)  # A4 size in points
        return PdfReader(open(pdf_path, "rb"))

def create_empty_pdf(filename, page_size=A4):
    writer = PdfWriter()
    writer.add_blank_page(*page_size)
    with open(filename, "wb") as f:
        writer.write(f)
    print(f"Empty PDF '{filename}' created successfully.")

def initialize_canvas():
    """Initialize canvas for drawing text with A4 page size."""
    return canvas.Canvas(io.BytesIO(), pagesize=A4)

def add_text_to_canvas(can, texts, color,alignment="left"):
    """Add text to the canvas of specified page."""
    can.setFont("Times-Roman", 12)
    can.setFillColor(color)
    for element in texts:
        if element:
            text, x, y, font_size = element
            can.setFontSize(font_size)
            if alignment == "left":
                can.drawString(x, y, str(text))
            elif alignment == "center":
                can.drawCentredString(x, y, str(text))
            elif alignment == "right":
                can.drawRightString(x, y, str(text))
            
            if DEBUG_MODE:
                print(text)
    can.showPage()
    can.save()

def add_block_to_canvas(can, blocks, color):
    """Add text to the canvas of specified page."""

    can.setStrokeColor('gray') 
    stroke = 1 if DEBUG_MODE else 0

    for element in blocks:
        set_color = color
        can.setFillColor(color)
        if element:
            if len(element) == 5:
                x, y, w, h, element_color = element
                set_color = element_color
                if element_color == 'transparent':         
                    can.rect(x,y,w,h, stroke=stroke, fill=0)
                    if DEBUG_MODE:
                        print(f"{set_color} block at ({x},{y},{w},{h})")
                    continue

                else:
                    can.setFillColor(element_color)
            elif len(element) == 4:
                x, y, w, h = element
            else:
                print(f'''ERROR-ERROR-ERROR-ERROR-ERROR-ERROR-ERROR: 
                      \n Wrong Format block found 
                      \n current block: {element}
                      \n please use [x,y,w,h] or [x,y,w,h,color] format
                      \n Skipping Current Block''')
                continue

            can.rect(x,y,w,h, stroke=stroke, fill=1)
            if DEBUG_MODE:
                print(f"{set_color} block at ({x},{y},{w},{h})")
    can.showPage()
    can.save()

def merge_pages(existing_pdf, output, packet, page_number):
    """Merge the modified page with the original PDF."""
    packet.seek(0)
    new_pdf = PdfReader(packet)
    for i, page in enumerate(existing_pdf.pages):
        if i == page_number:
            page.merge_page(new_pdf.pages[0])
        output.add_page(page)

def write_to_new_pdf(output, output_path):
    """Write the modified PDF to a new file."""
    with open(output_path, "wb") as f:
        output.write(f)

def add_text(texts=[[]],
             pdf_path=INPUT_FILE, 
             output_path=SYSTEM_FILE, 
             page_number=1, 
             color="black",
             alignment="left"):
    """Add text to the specified page of the PDF."""
    existing_pdf = open_pdf(pdf_path)
    page_number -= 1
    output = PdfWriter()
    can = initialize_canvas()
    add_text_to_canvas(can, texts, color,alignment)
    merge_pages(existing_pdf, output, can._filename, page_number)  # Pass page_number here
    write_to_new_pdf(output, output_path)


def add_block(blocks, pdf_path=SYSTEM_FILE, output_path=SYSTEM_FILE, page_number=1, color='black'):
    existing_pdf = open_pdf(pdf_path)
    page_number -= 1
    output = PdfWriter()
    can = initialize_canvas()
    add_block_to_canvas(can, blocks, color)
    merge_pages(existing_pdf, output, can._filename, page_number)  # Pass page_number here
    write_to_new_pdf(output, output_path)

# Example usage:
'''texts = [
    ["Hello", 100, 700, 12],
    ["World!", 200, 700, 12]
]

blocks = [
    [100,100,100,100,'black']
]
'''

if __name__ == "__main__":
    print("I told you to run overlays.py, DO NOT FUCK WITH THIS MODULE")