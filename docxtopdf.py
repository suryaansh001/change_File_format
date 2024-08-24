from docx2pdf import convert

# Function to convert docx to pdf
def convert_docx_to_pdf(docx_path, pdf_path=None):
    """
    Convert a .docx file to .pdf file.

    :param docx_path: Path to the .docx file to convert.
    :param pdf_path: (Optional) Path to save the converted .pdf file. If None, saves in the same directory.
    """
    convert(docx_path, pdf_path)
    print(f"Converted '{docx_path}' to '{pdf_path or docx_path.replace('.docx', '.pdf')}'")

# Example usage
docx_file_path = "enter the path of the file in docx format"
pdf_file_path = "name of the pdf file (you amy enter it a path to it if you want)"  # Optional
convert_docx_to_pdf(docx_file_path, pdf_file_path)