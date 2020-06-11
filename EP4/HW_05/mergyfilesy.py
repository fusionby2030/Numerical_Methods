from PyPDF2 import PdfFileMerger

pdfs = ['/home/fusionby2030/Uni_Ausgabe/TP/EPSON001.PDF', '/home/fusionby2030/Uni_Ausgabe/TP/EPSON002.PDF', '/home/fusionby2030/Uni_Ausgabe/TP/EPSON003.PDF', '/home/fusionby2030/Uni_Ausgabe/TP/EPSON004.PDF', '/home/fusionby2030/Uni_Ausgabe/TP/EPSON005.PDF']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("/home/fusionby2030/Uni_Ausgabe/TP/3707437_HW06.pdf")
merger.close()


"""

for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    if pagenum % 2:
        page.rotateClockwise(180)
    pdf_writer.addPage(page)

"""
