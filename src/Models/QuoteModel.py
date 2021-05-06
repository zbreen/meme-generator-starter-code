"""What a quote should look like."""
class QuoteModel:
    def __init__(self, body="", author=""):
        """Initialize values."""
        self.body = body
        self.author = author

    def __repr__(self):
        """What the quote should look like."""
        return f"{self.body} - {self.author}"