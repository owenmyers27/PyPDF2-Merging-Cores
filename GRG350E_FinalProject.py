from PyPDF2 import PdfFileMerger
from os import listdir
input_dir = r"C:\Users\Owen\Desktop\GLO\TxSED\GRG_350E\All_pages"

merger = PdfFileMerger()

count = 100
while count <= 129:
    merge_list = []
    for x in listdir(input_dir):
        x.startswith('13-A' + str(count)):
        merge_list.append(input_dir + x)
    for pdf in merge_list:
        if count >= 100
        merger.append(pdf)
        merger.write(f"C:\Users\Owen\Desktop\GLO\TxSED\GRG_350E\MergedCores\13-A{str(count)}.pdf"))
        merger.close()
        count += 1

