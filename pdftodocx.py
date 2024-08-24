from pdf2docx import Converter

pdf_file_path = "path_to.pdf"
docx_file_path = "path/name_to.docx"

# Create a PDF to DOCX converter
cv = Converter(pdf_file_path)

# Convert PDF to DOCX
cv.convert(docx_file_path, start=0, end=None)

# Close the converter
cv.close()
