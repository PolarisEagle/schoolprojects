import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_to_pdf(file_path):
    # Open the .py file and read its contents
    with open(file_path, 'r') as f:
        contents = f.read()

    # Set up the PDF canvas
    pdf_file_name = os.path.splitext(file_path)[0] + '.pdf'
    c = canvas.Canvas(pdf_file_name, pagesize=letter)

    # Split the contents of the .py file into lines
    lines = contents.split('\n')

    # Set the initial y-coordinate of the text object
    y = 750

    # Write the .py file contents to the PDF file
    for line in lines:
        # Check if the line will fit on the current page
        if y < 50:
            # If not, create a new page and reset the y-coordinate
            c.showPage()
            y = 750
        textobject = c.beginText()
        textobject.setTextOrigin(50, y)
        textobject.textLine(line)
        c.drawText(textobject)
        y -= 15

    # Save the PDF file
    c.save()


if __name__ == '__main__':
    file_path = input('Enter the path to the .py file to convert: ')
    convert_to_pdf(file_path)
    print('Conversion complete.')
