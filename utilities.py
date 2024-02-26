from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io

def open_pdf(pdf_path):
    """Open PDF file and return PdfReader object."""
    return PdfReader(open(pdf_path, "rb"))

def initialize_canvas():
    """Initialize canvas for drawing text with A4 page size."""
    return canvas.Canvas(io.BytesIO(), pagesize=A4)

def add_text_to_canvas(can, texts, page_number):
    """Add text to the canvas of specified page."""
    can.setFont("Helvetica", 12)
    for text, x, y, font_size in texts:
        can.setFontSize(font_size)
        can.drawString(x, y, text)
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

def add_text(pdf_path, texts, output_path="output.pdf", page_number=1):
    """Add text to the specified page of the PDF."""
    existing_pdf = open_pdf(pdf_path)
    page_number -= 1
    output = PdfWriter()
    can = initialize_canvas()
    add_text_to_canvas(can, texts, page_number)  # Pass page_number here
    merge_pages(existing_pdf, output, can._filename, page_number)  # Pass page_number here
    write_to_new_pdf(output, output_path)

# Example usage:
texts = [
    ["Hello", 100, 700, 12],
    ["World!", 200, 700, 12]
]

if __name__ == "__main__":
    print("I told you to run overlays.py, DO NOT FUCK WITH THIS MODULE")