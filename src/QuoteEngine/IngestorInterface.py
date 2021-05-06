"""The base form of the Ingestor."""
from abc import ABC, abstractmethod

from typing import List
from QuoteModel import QuoteModel

class IngestorInterface:
    """A class that sees whether a file is ingestible,
    parses depending on filetype.
    """

    @classmethod
    def can_ingest(clr, path) -> bool:
        """Check that file is ingestible."""
        return path in ingestible.values()

    # this is to be overwritten
    @classmethod
    def parse(clr, path: str) -> List[QuoteModel]:
        """Get info from the file.

        It's blank here so it can be overwritten in other filetypes.
        """
        pass
