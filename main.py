import os
import glob
from PyPDF2 import PdfMerger, PdfReader

# Get the current directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Search for all PDF files in the script directory and subdirectories
pdf_files = glob.glob(f'{script_dir}/**/*.pdf', recursive=True)

# Create the merger object to merge the PDFs
merger = PdfMerger()

# Prepare the index file
index_txt = "documents_index.txt"
with open(index_txt, "w") as index:
    # Initial page number for the current document in the merged PDF
    current_page = 1

    for pdf in pdf_files:
        # Add the PDF to the merged document
        merger.append(pdf)
        
        # Get the number of pages of the current PDF
        with open(pdf, "rb") as f:
            reader = PdfReader(f)
            num_pages = len(reader.pages)
        
        # Write to the index the file name and the initial page
        index.write(f"{os.path.basename(pdf)}: Initial Page {current_page}\n")
        
        # Update the initial page number for the next document
        current_page += num_pages

# Save the merged PDF
output_pdf = "merged_documents.pdf"
merger.write(output_pdf)
merger.close()

print(f"Merged PDF '{output_pdf}' and its index '{index_txt}' have been created.")
