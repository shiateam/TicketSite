import pdfkit
config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
<<<<<<< HEAD
# pdfkit.from_string(index.html, 'MyPDF.pdf', configuration=config)

# pdfkit.from_string('hello','string.pdf')


pdfkit.from_file('index.html','file.pdf',configuration=config)
# pdfkit.from_url("http://google.com", "out.pdf")
=======
def get_pdf(template):

# pdfkit.from_string(index.html, 'MyPDF.pdf', configuration=config)

# pdfkit.from_string('hello','string.pdf')
    return  pdfkit.from_file(template, 'file.pdf', configuration=config)
# pdfkit.from_url("http://www.shadiafarinan.ir/orders/create/307", "out.pdf",configuration=config)
# url=http.//en.wikipe

>>>>>>> one
