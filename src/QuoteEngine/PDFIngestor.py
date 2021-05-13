"""An ingestor for reading pdf files."""
import os
import subprocess
import random

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class PDFIngestor(IngestorInterface):
    """The class that ingests info from pdf."""

    # https://knowledge.udacity.com/questions/572306

    @classmethod
    def parse(cls, path):
        """Parse form a pdf file."""
        quotes = []
        try:
            tmp = f'./_data/DogQuotes/{random.randint(0, 1000)}.txt'
            call = subprocess.call(['pdftotext', path, tmp])
            file_ref = open(tmp, "r")
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    q = QuoteModel(parse[0].strip(), parse[1].strip())
                    quotes.append(q)
            file_ref.close()
            os.remove(tmp)
            # print(quotes)
        except Exception as e:
            raise Exception("pdf parsing issue occured.")
        return quotes
