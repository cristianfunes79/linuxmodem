import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--doc', help='PDF Document to be parsed', dest='pdf_file')

args = parser.parse_args()
print(args.pdf_file)

file_d = open(args.pdf_file, 'rb')
pdf_document = PDFDocument(file_d)
viewer_document = SimplePDFViewer(file_d)

doc_pages = []

for index in range(1, len([p for p in pdf_document.pages()]) ):
    print('PAGE {}'.format(index))
    #starts parsing page by page
    viewer_document.navigate( index )
    viewer_document.render()
    doc_pages.append( "".join(viewer_document.canvas.strings))


filew = open('/home/cristianfunes/output.txt','w')
for item in doc_pages:
    filew.write(item)
    
file_d.close()
filew.close()

#document = open()
