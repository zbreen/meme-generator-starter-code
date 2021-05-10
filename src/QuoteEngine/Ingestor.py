"""The file that determines which ingestor to use."""
import os

from .IngestorInterface import IngestorInterface
from .TextIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .CSVIngestor import CSVIngestor

ingestible = {
    "TEXT": ".txt",
    "CSV": ".csv",
    "PDF": ".pdf",
    "DOCX": ".docx",
}


class Ingestor(IngestorInterface):
    """The class that chooses which ingestor type to use."""

    @classmethod
    def parse(cls, path):
        """Get the file, then see what should parse it."""
        filename, file_extension = os.path.splitext(path)
        if not Ingestor.can_ingest(file_extension):
            raise ValueError("Unsupported file extension:", file_extension)
        if file_extension == ingestible.get("TEXT"):
            return TextIngestor.parse(path)
        if file_extension == ingestible.get("DOCX"):
            return DocxIngestor.parse(path)
        if file_extension == ingestible.get("PDF"):
            return PDFIngestor.parse(path)
        if file_extension == ingestible.get("CSV"):
            return CSVIngestor.parse(path)
