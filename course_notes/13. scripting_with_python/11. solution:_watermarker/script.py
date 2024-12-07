#  ==== solution: watermarker: ====

# this is the path for this
# michaeldugan@Michaels-MacBook-Pro ztm_python_course_notes % cd course_notes/13.\ scripting_with_python/11.\ solution:_watermarker

import PyPDF2

template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)
