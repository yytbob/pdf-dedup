# Function to deduplicate PDF pages
# Assistance provided by GPT-4 by OpenAI

import PyPDF2

def deduplicate_pdf(input_path, output_path):
    pdf_reader = PyPDF2.PdfReader(open(input_path, 'rb'))
    pdf_writer = PyPDF2.PdfWriter()

    seen_pages = set()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page_data = page.extract_text()

        if page_data not in seen_pages:
            seen_pages.add(page_data)
            pdf_writer.add_page(page)

    with open(output_path, 'wb') as out_file:
        pdf_writer.write(out_file)

# Example usage:
input_pdf_path = 'input.pdf'
output_pdf_path = 'output.pdf'
deduplicate_pdf(input_pdf_path, output_pdf_path)