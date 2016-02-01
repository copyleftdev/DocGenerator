#!/usr/bin/env python
import argparse
from faker import Factory
from docx import Document

"""Document Generation Utility"""

fake = Factory.create()


def gen_txt_file(fileN, dest, pii=False):
    """Generate text file requires parameters filename, destination, also a boolean
        enable or disable the generation of Psuedo PII Data: gen_txt_file("test1","data/",True)
    """
    if pii == False:

        with open('{}/{}'.format(dest,fileN),'w') as txtout:
            txtout.writelines(fake.text())

    elif pii == True:

        with open('{}/{}'.format(dest,fileN),'w') as txtout:
            txtout.writelines(fake.credit_card_full(card_type=None))




def gen_docx_file(fileN, dest, pii=False):
    pass

def gen_xlsx_file(fileN, dest, pii=False):
    pass

def gen_pdf_file(fileN, dest, pii=False):
    pass

def gen_pptx_file(fileN, dest, pii=False):
    pass

def main():
    parser = argparse.ArgumentParser(description='Generate Documents')
