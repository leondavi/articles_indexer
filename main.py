
import os
import re #Regular Expression lib
import pandas as pd

cwd = os.getcwd()
NULL_IDX = -1

'''
Return -1 if there is no regex of [Number] 
Return Reference number if regex of [Number] exists
'''
def check_if_contain_ref_num(name):
    regex = re.compile(r'\[(\d*)\]')
    match = regex.search(name)
    if match != None:
        ref_string = name[match.start():match.end()]
        ref_string = ref_string.replace("[","").replace("]","")
        return int(ref_string)
    return NULL_IDX

def get_pdf_files():
    pdf_files = []
    for filename in os.listdir(cwd):
        if filename.endswith(".pdf"):
            pdf_files.append(filename)
    return pdf_files

articles_list = get_pdf_files()
existed_ref_indexes = []
series = pd.Se

for pdf_file in articles_list:
    ref_status = check_if_contain_ref_num(pdf_file)
    if(ref_status == NULL_IDX):
        existed_ref_indexes.append(ref_status)

    res = check_if_contain_ref_num(pdf_file)


ep = 0


