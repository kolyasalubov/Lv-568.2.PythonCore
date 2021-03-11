# 1 colum - kanji
# 3 colum - level
# 19 colum - chinese reading (onyoumi)
# 22 colum - japanese reading (kunyomi)


import xlrd

workbook = xlrd.open_workbook(r"kanji.xls")
ragged_rows = True
sheet = workbook.sheet_by_index(0)
row_count = sheet.nrows
col_count = sheet.ncols
#counted the number of colums and rows

header = sheet.row_values(0, start_colx=0, end_colx=None)

#col_a = sheet.col_slice(1, start_rowx=0, end_rowx=None)
#col_a = sheet.col_values(1, start_rowx=1, end_rowx=None)
#перша цифра - номер колонки, далі з якого і по який рядок
#print(col_a)

###########################################################
#reading type: 1 fron on reading and any other number for kun reading
def getting_kanji (needed_level):
       
    #searching each kanji that represent needed level
    levels = []
    for i in sheet.col_values(3, start_rowx=1, end_rowx=None):
        levels.append(int(i))

    iteration = 0
    dictionary = {}
    for level in levels:
        iteration+=1
        if level == int(needed_level):
            kanji = (sheet.col_values(1, start_rowx=iteration, end_rowx=iteration+1))
            translation = (sheet.col_values(23, start_rowx=iteration, end_rowx=iteration+1))
            if translation[0]!= '-':
                dictionary[kanji[0]] = translation[0]
    return dictionary
#print(getting_kanji(1))
#found the needed level and took kanji and its translation
####################################################################