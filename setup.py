from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="docx-footer-extractor",
    version="1.0.0",
    author="Sunil K Sundaram",
    author_email="sunilsmindspace@gmail.com",
    description="A Python library for extracting metadata from DOCX file footers using parallel processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sunilsmindspace/docx-footer-extractor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    keywords="docx, metadata, footer, parallel, extraction, office, documents",
    project_urls={
        "Bug Reports": "https://github.com/sunilsmindspace/docx-footer-extractor/issues",
        "Source": "https://github.com/sunilsmindspace/docx-footer-extractor",
    },
)