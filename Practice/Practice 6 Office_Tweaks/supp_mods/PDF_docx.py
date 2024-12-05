from docx2pdf import convert
from pdf2docx import Converter
from supp_mods import files


def pdf_to_docx():
    docs = files.find_files('.pdf', type=0)
    if docs == {}:
        pass
    else:
        while True:
            choice = input('Выберите документ, который необходимо конвентировать в .docx (выберите 0, если необходимо конвентировать все): ')
            if not choice.isdigit() or (int(choice) not in list(docs.keys()) and int(choice) != 0):
                print('Выбран неправильный документ!')
            else:
                break
        if int(choice) == 0:
            for i in list(docs.values()):
                pdf_file = i
                docx_file = pdf_file[:-3] + 'docx'
                pdf_conv = Converter(pdf_file)
                pdf_conv.convert(docx_file)
                pdf_conv.close()
                print(f'Файл {pdf_file} успешно конвертирован')
        else:
            pdf_file = docs.get(int(choice))
            docx_file = pdf_file[:-3] + 'docx'
            pdf_conv = Converter(pdf_file)
            pdf_conv.convert(docx_file)
            pdf_conv.close()
            print(f'Файл {pdf_file} успешно конвертирован')


def docx_to_pdf():
    docs = files.find_files('.docx', type=0)
    if docs == {}:
        pass
    else:
        while True:
            choice = input(
                'Выберите документ, который необходимо конвентировать в .pdf (выберите 0, если необходимо конвентировать все): ')
            if not choice.isdigit() or (int(choice) not in list(docs.keys()) and int(choice) != 0):
                print('Выбран неправильный документ!')
            else:
                break
        if int(choice) == 0:
            for i in list(docs.values()):
                docx_file = i
                pdf_file = docx_file[:-4] + 'pdf'
                convert(docx_file, pdf_file)
                print(f'Файл {docx_file} успешно конвертирован')
        else:
            docx_file = docs.get(int(choice))
            pdf_file = docx_file[:-4] + 'pdf'
            convert(docx_file, pdf_file)
            print(f'Файл {docx_file} успешно конвертирован')