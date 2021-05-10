"""Test the code."""
from .Ingestor import Ingestor

quotes = ['../_data/DogQuotes/DogQuotesTXT.txt',
          '../_data/DogQuotes/DogQuotesDOCX.docx',
          '../_data/DogQuotes/DogQuotesPDF.pdf',
          '../_data/DogQuotes/DogQuotesCSV.csv']

for q in quotes:
    try:
        print(Ingestor.parse(q))
    except ValueError as error:
        print(f"ValueError: {error}")
