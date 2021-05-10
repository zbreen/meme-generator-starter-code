"""An ingestor for reading csv files."""
import pandas as pd

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """The class that ingests info from csv."""

    @classmethod
    def parse(cls, path):
        """Parse from csv file."""
        # get file
        csv = pd.read_csv(path)
        quotes = []
        # iterate through file
        for index, row in csv.iterrows():
            q = QuoteModel(row['body'].strip(), row['author'].strip())
            quotes.append(q)
        return quotes
