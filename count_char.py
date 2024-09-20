import fitz  # PyMuPDF


def count_characters_in_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    total_characters = 0

    # Iterate through each page
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")  # Extract text from the page

        # Remove spaces and count characters
        text_without_spaces = text.replace(" ", "")  # Remove spaces
        total_characters += len(
            text_without_spaces
        )  # Count the characters excluding spaces

    pdf_document.close()
    return total_characters


# Example usage
pdf_path = "facr_cx_fs24_ht_fhnw.pdf"  # Replace with your PDF file path
character_count = count_characters_in_pdf(pdf_path)
print(
    f"Total number of characters in the PDF (excluding spaces): {character_count}"
)
