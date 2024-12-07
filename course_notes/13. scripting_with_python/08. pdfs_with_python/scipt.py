# ==== PDFs with python ====

# use this to get to the right directory in the terminal
# michaeldugan@Michaels-MacBook-Pro ztm_python_course_notes % cd course_notes/13.\ scripting_with_python/08.\ pdfs_with_python

import PyPDF2

# with open('./dummy.pdf', 'r') as file:
#     print(file)
# <_io.TextIOWrapper name='./dummy.pdf' mode='r' encoding='UTF-8'>


# Open the PDF file
with open('./dummy.pdf', 'rb') as file:  # Use 'rb' for reading binary files
    reader = PyPDF2.PdfReader(file)  # Use PdfReader instead of PdfFileReader

    # Example: Access the number of pages
    print(f"Number of pages: {len(reader.pages)}")

    # Example: Extract text from the first page
    first_page = reader.pages[0]
    print(first_page.extract_text())

with open('./twopage.pdf', 'rb') as file:  # Use 'rb' for reading binary files
    reader = PyPDF2.PdfReader(file)  # Use PdfReader instead of PdfFileReader

    # Example: Access the number of pages
    print(f"Number of pages: {len(reader.pages)}")

    # Example: Extract text from the first page
    first_page = reader.pages[0]
    print(first_page.extract_text())


# == rotate ==

# Open the source PDF
with open('./dummy.pdf', 'rb') as infile:
    reader = PyPDF2.PdfReader(infile)
    writer = PyPDF2.PdfWriter()

    # Rotate all pages 90 degrees clockwise
    for page in reader.pages:
        page.rotate(90)  # Rotate the page 90 degrees
        writer.add_page(page)

    # Save the rotated PDF to a new file
    with open('./tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

print("PDF has been rotated and saved as 'rotated_dummy.pdf'")
