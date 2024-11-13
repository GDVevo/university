def load_top_record():
    """
    Загружает высший рекорд из файла records.txt
    :return:
    """
    file = open('required_libs\\records.txt', 'r')
    top = file.readline()
    if top != '':
        print('Высший рекорд:', top)
