# PDF Page Deduplication Tool

This Python script removes duplicate pages from a PDF file by comparing the text content of each page. It utilizes the `PyPDF2` library to read and write PDF files.

## How It Works

The script works as follows:
1. **Read the PDF**: The input PDF file is read using the `PyPDF2.PdfReader`.
2. **Extract Text**: Text content from each page is extracted.
3. **Detect Duplicates**: Pages with identical text content are considered duplicates.
4. **Write Unique Pages**: Unique pages are written to a new PDF file using `PyPDF2.PdfWriter`.

## Usage

### 1. Prerequisites

Ensure you have Python installed on your system. This script is compatible with Python 3.

### 2. Install Dependencies

Install the `PyPDF2` library using `pip`: 

`pip install PyPDF2`

### Running the Script

1. Download `pdf-dedup.py` 
2. Rename your source PDF file to `input.pdf` and copy it to the directory of `pdf-dedup.py` 
3. Then, run the script: `python pdf-dedup.py`
4. Finally, the deduplicated PDF file will be saved as `output.pdf` in the same directory

### Cautions and Warnings

• **Text Extraction Limitations**: The deduplication is based on text extraction, so pages that appear visually identical but have different underlying text (e.g., images or different formatting) may not be detected as duplicates.

• **Incomplete Text Extraction**: Some complex PDFs may have text extraction issues, resulting in incomplete or inaccurate deduplication.

• **Dependency on PyPDF2**: The script relies on the PyPDF2 library, which may have its own limitations and bugs.

## Tips for Effective Deduplication

• **Backup**: Always keep a backup of the original PDF.

• **Automate Cautiously**: Automated tools and scripts can sometimes miss duplicates that are visually identical but slightly different at a byte level. If possible, verify the results manually.

• **Check Page Resequencing**: Ensure that removing duplicates doesn’t disrupt the document's logical sequence.

## Acknowledgments

This project has benefited from the assistance of GPT-4, an AI language model developed by OpenAI, for guidance in code structuring and implementation.

## License

This project is licensed under the GNU General Public License (Version 3). You may modify the content to better suit your preferences.
