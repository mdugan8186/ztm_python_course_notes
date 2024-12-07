# ==== exercise: pdf merger ====

# this is for the filepath
# michaeldugan@Michaels-MacBook-Pro ztm_python_course_notes % cd course_notes/13.\ scripting_with_python/09.\ exercise:_pdf_merger

import PyPDF2
import sys

inputs = sys.argv[1:]  # this will grab all the arguments besides the first one


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')
    merger.close()


# check if the program is working initially then to run the file afterwards to merge the pdfs
pdf_combiner(inputs)
# run this command in the terminal to see the output
# python3 script.py dummy.pdf twopage.pdf tilt.pdf
