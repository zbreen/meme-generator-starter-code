"""An ingestor for reading docx files."""
from typing import List
import docx

from QuoteModel import QuoteModel
from IngestorInterface import IngestorInterface


class DocxIngestor(IngestorInterface):
    """The class that ingests info from docx."""

    @classmethod
    def parse(cls, path):
        """Parse from docx file."""
        # get document
        doc = docx.Document(path)
        quotes = []
        # iterate through document
        for paragraph in doc.paragraphs:
            if paragraph.text != "":
                p = paragraph.text.split(' - ')
                q = QuoteModel(p[0].strip(), p[1].strip())
                quotes.append(q)
        return quotes
