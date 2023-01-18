import pandas
import sys
import os
import glob
from pathlib import Path

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

writer = pandas.ExcelWriter('vehiclesedited.xlsx')  # Arbitrary output name
for csvfilename in all_filenames:
    txt = Path(csvfilename).read_text()
    txt = txt.replace(',', '.')

    text_file = open(csvfilename, "w")
    text_file.write(txt)
    text_file.close()

    print("Loading " + csvfilename)
    df = pandas.read_csv(csvfilename, sep=';', encoding='utf-8')

    df.to_excel(writer, sheet_name=os.path.splitext(csvfilename)[0])
    print("done")
writer.save()
print("task completed")
