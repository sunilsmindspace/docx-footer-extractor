from docx_footer_extractor import DocxFooterExtractor

# Create extractor
extractor = DocxFooterExtractor(max_workers=4)

# Process folder or file list
results = extractor.extract("./data")

# print it
print(f'Results: \n {results}')
