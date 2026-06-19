import pymupdf4llm

def extract_pdf(pdf_path):

    markdown = pymupdf4llm.to_markdown(pdf_path)

    with open(
        "sections/document.md",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(markdown)

    return markdown