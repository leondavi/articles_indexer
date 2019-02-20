
import os
import re #Regular Expression lib

cwd = os.getcwd()


def check_if_contain_ref_num(name):
    regex = re.compile(r'\[(\d*)\]')
    match = regex.search(name)
    if match != None:
        return match.start() == 0
    return False

def get_pdf_files():
    pdf_files = []
    for filename in os.listdir(cwd):
        if filename.endswith(".pdf"):
            pdf_files.append(filename)
    return pdf_files


articles_list = get_pdf_files()

for pdf_file in articles_list:
    res = check_if_contain_ref_num(pdf_file)


ep = 0


