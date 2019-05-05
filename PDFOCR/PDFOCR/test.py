
from PyPDF2 import PdfFileReader

pdf = PdfFileReader(open("sample.pdf", "rb"))

    # Iterate pages
content = ""
for i in range(0, pdf.getNumPages()):

        # Extract text from page and add to content

	content += pdf.getPage(i).extractText() + "\n"


f=open("result.txt",'w')
f.write(content)

f.close