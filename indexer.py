
import os
import re #Regular Expression lib
import pandas as pd
import numpy as np

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

def split_ref_number(name_with_ref_num):
    regex = re.compile(r'\[(\d*)\]')
    match = regex.search(name_with_ref_num)
    if match != None:
        ref_string = name_with_ref_num[match.start():match.end()]
        name_without_ref_num = name_with_ref_num.replace(ref_string, "")
        ref_string = ref_string.replace("[", "").replace("]", "")
        return int(ref_string),name_without_ref_num.lstrip() #return reference number and the name without the reference
    return name_with_ref_num

def get_pdf_files():
    pdf_files = []
    for filename in os.listdir(cwd):
        if filename.endswith(".pdf"):
            pdf_files.append(filename)
    return pdf_files


def find_exluded_files(articles_list):
    existed_ref_indexes = []
    for pdf_file in articles_list:
        ref_status = check_if_contain_ref_num(pdf_file)
        if(ref_status != NULL_IDX):
            existed_ref_indexes.append(ref_status)

    return existed_ref_indexes



#Renaming and generating dictionary by ref number
def renaming_articles_names(articles_list):
    articles_list_by_ref_num = dict()
    excluded_list = find_exluded_files(articles_list)
    curr_ref_num = 1
    for pdf_file in articles_list:
        ref_status = check_if_contain_ref_num(pdf_file)
        if ref_status == NULL_IDX:
            #finding available reference number
            while curr_ref_num in excluded_list:
                curr_ref_num+=1
            os.rename(pdf_file,"["+str(curr_ref_num)+"] "+pdf_file)
            articles_list_by_ref_num[curr_ref_num] = pdf_file
            curr_ref_num += 1
        else:
            ref_num,article_without_ref = split_ref_number(pdf_file)
            articles_list_by_ref_num[ref_num] = article_without_ref

    return articles_list_by_ref_num

def main():
    print("Generating articles list")
    articles_list = get_pdf_files()
    print("Renaming, adding refrences indexes")
    articles_dict = renaming_articles_names(articles_list)

    print("Articles: \n----------\n\n")
    print("{:<8} {:<15}".format('[#]','Article'))
    for k,v in sorted(articles_dict.items()):
        print("{:<8} {:<15}".format(k, v))

if __name__ == '__main__':
    main()




ep = 0

