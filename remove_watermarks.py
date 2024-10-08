import fitz  # PyMuPDF
import requests

def remove_watermarks(input_pdf_path, output_pdf_path):
    pdf_document = fitz.open(input_pdf_path)

    for page in pdf_document:
        text_blocks = page.get_text("blocks")

        for block in text_blocks:
            if 'WATERMARK' in block[4]:  # Change 'WATERMARK' to your watermark text
                page.delete_text(block[:4])

        for img_index in range(len(page.get_images(full=True))):
            img = page.get_images(full=True)[img_index]
            xref = img[0]
            page.delete_image(xref)

    pdf_document.save(output_pdf_path)
    pdf_document.close()
    print(f"Watermarks removed and saved to {output_pdf_path}")

def download_pdf(url, output_path):
    response = requests.get(url)
    with open(output_path, 'wb') as f:
        f.write(response.content)

if __name__ == "__main__":
    # Replace with the URL of the PDF to download and watermark removal text
    pdf_url = "https://example.com/your-pdf.pdf"  # Change to your PDF URL
    downloaded_pdf = "downloaded.pdf"
    output_pdf = "output.pdf"

    download_pdf(pdf_url, downloaded_pdf)
    remove_watermarks(downloaded_pdf, output_pdf)
