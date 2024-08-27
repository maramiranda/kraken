import pytesseract
from pdf2image import convert_from_path
import os

# Specify the path to the PDF file
pdf_path = 'WellpathAlamedaACSO2022-compressed.pdf'
  # Use the raw string to handle backslashes

# Convert PDF to images
pages = convert_from_path(pdf_path, 300)  # DPI = 300

# Iterate through all the pages and perform OCR
for page_num, page in enumerate(pages):
    # Save each page as an image
    image_path = f'page_{page_num + 1}.png'
    page.save(image_path, 'PNG')

    # Perform OCR on the image
    text = pytesseract.image_to_string(page)

    # Save the extracted text to a file
    with open(f'page_{page_num + 1}_output.txt', 'w') as f:
        f.write(text)

    # Optionally, clean up the image file after processing
    os.remove(image_path)
